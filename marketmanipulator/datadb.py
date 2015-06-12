__author__ = 'Zivia'

import psycopg2
from psycopg2.extras import Json
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys


def version():

    connection = None

    try:

        connection = psycopg2.connect(database='market_manipulator', user='Zivia')
        cur = connection.cursor()

        cur.execute('SELECT version()')

        print cur.fetchone()

    except psycopg2.DatabaseError, e:

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def create_database(name="market_manipulator"):

    connection = None

    try:

        connection = psycopg2.connect("dbname='postgres' user='Zivia'")
        cur = connection.cursor()

        print 'Creating database: ' + name

        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute("CREATE DATABASE " + name)

    except psycopg2.DatabaseError, e:

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def create_table(name="default"):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        print 'Creating table: ' + name

        cur.execute("CREATE TABLE " + name + " (id integer, data json)")

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def drop_table(name="default"):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        print 'Dropping table: ' + name

        cur.execute("DROP TABLE IF EXISTS " + name)

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def insert(items=[], commerce_listings=[], commerce_prices=[]):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        for item in items:

            cur.execute("INSERT INTO items (id, data) VALUES (%s, %s)", [item[u'id'], Json(item)])

        for commerce_listing in commerce_listings:

            cur.execute("INSERT INTO commerce_listings (id, data) VALUES (%s, %s)", [commerce_listing[u'id'], Json(commerce_listing)])

        for commerce_price in commerce_prices:

            cur.execute("INSERT INTO commerce_prices (id, data) VALUES (%s, %s)", [commerce_price[u'id'], Json(commerce_price)])

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def remove(items_ids=[], commerce_listings_ids=[], commerce_prices_ids=[]):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        for item_id in items_ids:

            cur.execute("DELETE FROM items WHERE id = (%s)", [item_id])

        for commerce_listing_id in commerce_listings_ids:

            cur.execute("DELETE FROM commerce_listings WHERE id = (%s)", [commerce_listing_id])

        for commerce_price_id in commerce_prices_ids:

            cur.execute("DELETE FROM commerce_prices WHERE id = (%s)", [commerce_price_id])

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()

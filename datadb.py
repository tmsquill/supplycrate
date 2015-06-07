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


def create_table(name="default"):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        print 'Creating table: ' + name

        cur.execute("CREATE TABLE " + name + " (id serial, data json)")

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def insert_item(id=None, item=None):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        cur.execute("INSERT INTO items (id, data) VALUES (%s, %s)", [id, Json(item)])

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def insert_commerce_listing(id=None, listing=None):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        cur.execute("INSERT INTO commerce_listings (id, data) VALUES (%s, %s)", [id, Json(listing)])

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()


def insert_commerce_price(id=None, price=None):

    connection = None

    try:

        connection = psycopg2.connect("dbname='market_manipulator' user='Zivia'")
        cur = connection.cursor()

        cur.execute("INSERT INTO commerce_prices (id, data) VALUES (%s, %s)", [id, Json(price)])

        connection.commit()

    except psycopg2.DatabaseError, e:

        if connection:
            connection.rollback()

        print 'Database Error: %s' % e
        sys.exit(1)

    finally:

        if connection:
            connection.close()

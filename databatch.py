__author__ = 'Zivia'

import items as it
import tradingpost as tp
import datadb as db
import dataservice as ds
import datautils as du


def all_items(purge=False):

    if purge:

        db.drop_table('items')
        db.create_table('items')

    items_ids = du.chunks(it.items(), 200)

    for items_id_group in items_ids:

        items = it.items(items_id_group)

        print ds.pretty_json(items)

        for item in items:

            id = item[u'id']

            print 'Processing item: ' + str(id)

            db.insert_item(id, item)


def all_commerce_listings(purge=False):

    if purge:

        db.drop_table('commerce_listings')
        db.create_table('commerce_listings')

    listings_ids = du.chunks(tp.commerce_listings(), 200)

    for listings_id_group in listings_ids:

        listings = tp.commerce_listings(listings_id_group)

        print ds.pretty_json(listings)

        for listing in listings:

            id = listing[u'id']

            print 'Processing listing: ' + str(id)

            db.insert_commerce_listing(id, listing)


def all_commerce_prices(purge=False):

    if purge:

        db.drop_table('commerce_prices')
        db.create_table('commerce_prices')

    prices_ids = du.chunks(tp.commerce_prices(), 200)

    for prices_id_group in prices_ids:

        prices = tp.commerce_prices(prices_id_group)

        print ds.pretty_json(prices)

        for price in prices:

            id = price[u'id']

            print 'Processing price: ' + str(id)

            db.insert_commerce_price(id, price)


if __name__ == "__main__":

    db.create_database()

    all_commerce_prices(purge=True)

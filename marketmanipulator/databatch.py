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

    commerce_items_ids = du.chunks(it.items(), 200)

    for commerce_items_id_group in commerce_items_ids:

        items = it.items(commerce_items_id_group)

        print ds.pretty_json(items)

        db.insert(items=items)


def all_commerce_listings(purge=False):

    if purge:

        db.drop_table('commerce_listings')
        db.create_table('commerce_listings')

    commerce_listings_ids = du.chunks(tp.commerce_listings(), 200)

    for commerce_listings_id_group in commerce_listings_ids:

        commerce_listings = tp.commerce_listings(commerce_listings_id_group)

        print ds.pretty_json(commerce_listings)

        db.insert(commerce_listings=commerce_listings)


def all_commerce_prices(purge=False):

    if purge:

        db.drop_table('commerce_prices')
        db.create_table('commerce_prices')

    commerce_prices_ids = du.chunks(tp.commerce_prices(), 200)

    for commerce_prices_id_group in commerce_prices_ids:

        commerce_prices = tp.commerce_prices(commerce_prices_id_group)

        print ds.pretty_json(commerce_prices)

        db.insert(commerce_prices=commerce_prices)


if __name__ == "__main__":

    all_items(purge=True)
    all_commerce_listings(purge=True)
    all_commerce_prices(purge=True)

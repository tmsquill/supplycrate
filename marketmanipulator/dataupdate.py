__author__ = 'Zivia'

import marketmanipulator.items as it
import marketmanipulator.tradingpost as tp
import marketmanipulator.datadb as db
import marketmanipulator.dataservice as ds
import marketmanipulator.datautils as du


def update_items(items_ids=None):

    if items_ids is None:

        db.drop_table('scratch_items')
        db.create_table(items_table_name='scratch_items')

        items_ids = du.chunks(it.items(), 200)

        for items_ids_group in items_ids:

            items = it.items(items_ids_group)

            print ds.pretty_json(items)

            db.insert(items=items, scratch=True)

        db.compare(items=True)

    else:

        items = it.items(items_ids)

        print ds.pretty_json(items)

        db.remove(items_ids=items_ids, scratch=True)
        db.insert(items=items, scratch=True)


def update_commerce_listings(commerce_listings_ids=None):

    if commerce_listings_ids is None:

        db.drop_table('scratch_commerce_listings_buy')
        db.drop_table('scratch_commerce_listings_sell')
        db.create_table(commerce_listings_table_name='scratch_commerce_listings')

        commerce_listings_ids = du.chunks(tp.commerce_listings(), 200)

        for commerce_listings_ids_group in commerce_listings_ids:

            commerce_listings = tp.commerce_listings(commerce_listings_ids_group)

            print ds.pretty_json(commerce_listings)

            db.insert(commerce_listings=commerce_listings, scratch=True)

        db.compare(commerce_listings=True)

    else:

        commerce_listings = tp.commerce_listings(commerce_listings_ids)

        print ds.pretty_json(commerce_listings)

        db.remove(commerce_listings_ids=commerce_listings_ids, scratch=True)
        db.insert(commerce_listings=commerce_listings, scratch=True)


def update_commerce_prices(commerce_prices_ids=None):

    if commerce_prices_ids is None:

        db.drop_table('scratch_commerce_prices')
        db.create_table(commerce_prices_table_name='scratch_commerce_prices')

        commerce_prices_ids = du.chunks(tp.commerce_prices(), 200)

        for commerce_prices_ids_group in commerce_prices_ids:

            commerce_prices = tp.commerce_prices(commerce_prices_ids_group)

            print ds.pretty_json(commerce_prices)

            db.insert(commerce_prices=commerce_prices, scratch=True)

        db.compare(commerce_prices=True)

    else:

        commerce_prices = tp.commerce_prices(commerce_prices_ids)

        print ds.pretty_json(commerce_prices)

        db.remove(commerce_prices_ids=commerce_prices_ids, scratch=True)
        db.insert(commerce_prices=commerce_prices, scratch=True)


if __name__ == "__main__":

    update_items()
    update_commerce_listings()
    update_commerce_prices()

__author__ = 'Zivia'

import supplycrate.endpoints.v2.items as it
import supplycrate.endpoints.v2.tradingpost as tp
import supplycrate.datadb as db
import supplycrate.datautils as du


def update_all():

    update_items()
    update_commerce_listings()
    update_commerce_prices()


def update_items(items_ids=None):

    if items_ids is None:

        db.drop_table('scratch_items')
        db.create_table(items_table_name='scratch_items')

        items_ids = it.items()

        items_ids_len = len(items_ids)
        items_ids_counter = 0

        items_ids_groups = du.chunks(items_ids, 200)

        for items_ids_group in items_ids_groups:

            items = it.items(items_ids_group)

            items_ids_counter += len(items_ids_group)
            du.print_update_progress(entity='Items', cur=items_ids_counter, max=items_ids_len)

            db.insert(items=items, scratch=True)

    else:

        items = it.items(items_ids)

        db.remove(items_ids=items_ids, scratch=True)
        db.insert(items=items, scratch=True)

    print


def update_commerce_listings(commerce_listings_ids=None):

    if commerce_listings_ids is None:

        db.drop_table('scratch_commerce_listings_buy')
        db.drop_table('scratch_commerce_listings_sell')
        db.create_table(commerce_listings_table_name='scratch_commerce_listings')

        commerce_listings_ids = tp.commerce_listings()

        commerce_listings_ids_len = len(commerce_listings_ids)
        commerce_listings_ids_counter = 0

        commerce_listings_ids_groups = du.chunks(commerce_listings_ids, 200)

        for commerce_listings_ids_group in commerce_listings_ids_groups:

            commerce_listings = tp.commerce_listings(commerce_listings_ids_group)

            commerce_listings_ids_counter += len(commerce_listings_ids_group)
            du.print_update_progress(entity='Commerce Listings', cur=commerce_listings_ids_counter, max=commerce_listings_ids_len)

            db.insert(commerce_listings=commerce_listings, scratch=True)

    else:

        commerce_listings = tp.commerce_listings(commerce_listings_ids)

        db.remove(commerce_listings_ids=commerce_listings_ids, scratch=True)
        db.insert(commerce_listings=commerce_listings, scratch=True)

    print


def update_commerce_prices(commerce_prices_ids=None):

    if commerce_prices_ids is None:

        db.drop_table('scratch_commerce_prices')
        db.create_table(commerce_prices_table_name='scratch_commerce_prices')

        commerce_prices_ids = tp.commerce_prices()

        commerce_prices_ids_groups = du.chunks(commerce_prices_ids, 200)

        commerce_prices_ids_len = len(commerce_prices_ids)
        commerce_prices_ids_counter = 0

        for commerce_prices_ids_group in commerce_prices_ids_groups:

            commerce_prices = tp.commerce_prices(commerce_prices_ids_group)

            commerce_prices_ids_counter += len(commerce_prices_ids_group)
            du.print_update_progress(entity='Commerce Price', cur=commerce_prices_ids_counter, max=commerce_prices_ids_len)

            db.insert(commerce_prices=commerce_prices, scratch=True)

    else:

        commerce_prices = tp.commerce_prices(commerce_prices_ids)

        db.remove(commerce_prices_ids=commerce_prices_ids, scratch=True)
        db.insert(commerce_prices=commerce_prices, scratch=True)

    print


if __name__ == "__main__":

    update_all()

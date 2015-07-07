__author__ = 'Zivia'

import datadb as db


class InvalidIdError(Exception):

    def __init__(self, value):

        self.value = value

    def __str__(self):

        return repr(self.value)


def search_all(ids=None, scratch=False):

    if not (isinstance(ids, list) and all(ids[x] > 0 for x in xrange(len(ids)))):

        raise InvalidIdError('input must be list of positive integers')

    search = db.select(items_ids=ids, commerce_listings_ids=ids, commerce_prices_ids=ids, scratch=scratch)

    return search


def search_items(ids=None, scratch=False):

    if not (isinstance(ids, list) and all(ids[x] > 0 for x in xrange(len(ids)))):

        raise InvalidIdError('input must be list of positive integers')

    items = db.select(items_ids=ids, scratch=scratch)

    return items[0]


def search_commerce_listings(ids=None, scratch=False):

    if not (isinstance(ids, list) and all(ids[x] > 0 for x in xrange(len(ids)))):

        raise InvalidIdError('input must be list of positive integers')

    commerce_listings = db.select(commerce_listings_ids=ids, scratch=scratch)

    return commerce_listings[1]


def search_commerce_prices(ids=None, scratch=False):

    if not (isinstance(ids, list) and all(ids[x] > 0 for x in xrange(len(ids)))):

        raise InvalidIdError('input must be list of positive integers')

    commerce_prices = db.select(commerce_prices_ids=ids, scratch=scratch)

    return commerce_prices[2]


if __name__ == "__main__":

    search_ids = [75, 97]

    print search_all(search_ids)
    print search_items(search_ids)
    print search_commerce_listings(search_ids)
    print search_commerce_prices(search_ids)
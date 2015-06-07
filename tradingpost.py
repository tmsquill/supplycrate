__author__ = 'Zivia'

import dataservice as ds


def commerce_listings(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/commerce/listings')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/commerce/listings?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/commerce/listings?ids=' + str(ids))


def commerce_exchange(coins=False, gems=False, quantity=0):

    if coins is True:

        return ds.pull_data('https://api.guildwars2.com/v2/commerce/exchange/coins?quantity=' + str(quantity))

    if gems is True:

        return ds.pull_data('https://api.guildwars2.com/v2/commerce/exchange/gems?quantity=' + str(quantity))


def commerce_prices(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/commerce/prices')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/commerce/prices?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/commerce/prices?ids=' + str(ids))

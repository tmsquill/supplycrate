__author__ = 'Zivia'

import dataservice as ds


def items(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/items')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/items?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/items?ids=' + str(ids))


def recipes(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/recipes')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/recipes?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/recipes?ids=' + str(ids))

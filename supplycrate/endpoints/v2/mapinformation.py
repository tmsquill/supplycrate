__author__ = 'Zivia'

import supplycrate.dataservice as ds


def continents(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/continents')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/continents?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/continents?ids=' + str(ids))


def maps(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/maps')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/maps?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/maps?ids=' + str(ids))

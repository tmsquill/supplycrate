__author__ = 'Zivia'

import supplycrate.dataservice as ds


def build():

    return ds.pull_data('https://api.guildwars2.com/v1/build')


def colors(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v1/colors')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v1/colors?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v1/colors?ids=' + str(ids))


def files(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v1/files')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v1/files?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v1/files?ids=' + str(ids))

__author__ = 'Zivia'

import supplycrate.dataservice as ds


def build():

    return ds.pull_data('https://api.guildwars2.com/v2/build')


def colors(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/colors')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/colors?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/colors?ids=' + str(ids))


def currencies(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/currencies')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/currencies?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/currencies?ids=' + str(ids))


def files(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/files')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/files?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/files?ids=' + str(ids))


def quaggans(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/quaggans')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/quaggans?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/quaggans?ids=' + str(ids))


def specializations(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/specializations')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/specializations?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/specializations?ids=' + str(ids))


def worlds(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/worlds')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/worlds?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/worlds?ids=' + str(ids))

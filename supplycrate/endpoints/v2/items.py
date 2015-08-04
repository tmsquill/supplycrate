__author__ = 'Zivia'

import supplycrate.dataservice as ds


def items(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/items')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/items?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/items?ids=' + str(ids))


def materials(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/materials')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/materials?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/materials?ids=' + str(ids))


def recipes(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/recipes')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/recipes?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/recipes?ids=' + str(ids))


def recipes_search(id=None, input=False, output=False):

    if id is None:

        return ds.pull_data('https://api.guildwars2.com/v2/recipes/search')

    else:

        if input:

            return ds.pull_data('https://api.guildwars2.com/v2/recipes/search?input=' + str(id))

        elif output:

            return ds.pull_data('https://api.guildwars2.com/v2/recipes/search?output=' + str(id))


def skins(ids=None):

    if ids is None:

        return ds.pull_data('https://api.guildwars2.com/v2/skins')

    else:

        if isinstance(ids, list):

            return ds.pull_data('https://api.guildwars2.com/v2/skins?ids=' + ','.join(map(str, ids)))

        else:

            return ds.pull_data('https://api.guildwars2.com/v2/skins?ids=' + str(ids))

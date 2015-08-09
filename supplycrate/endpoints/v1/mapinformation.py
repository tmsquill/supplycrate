__author__ = 'Zivia'

import supplycrate.dataservice as ds


def continents(lang=None):

    if lang is None:

        return ds.pull_data('https://api.guildwars2.com/v1/continents')

    return ds.pull_data('https://api.guildwars2.com/v1/continents?lang=' + str(lang))


def maps(map_id=None, lang=None):

    query = '?'

    if map_id is not None:

        query += 'map_id=' + str(map_id)

    if lang is not None:

        query += str('&lang=' + lang)

    return ds.pull_data('https://api.guildwars2.com/v1/maps' + query)


def map_floor(continent_id=None, floor=None, lang=None):

    if continent_id  is None or floor is None:

        return

    else:

        query = '?continent_id=' + str(continent_id) + '&floor=' + str(floor)

        if lang is not None:

            query += str('&lang=' + lang)

        return ds.pull_data('https://api.guildwars2.com/v1/map_floor' + query)

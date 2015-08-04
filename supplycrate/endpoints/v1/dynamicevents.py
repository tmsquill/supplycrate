__author__ = 'Zivia'

import supplycrate.dataservice as ds

def events():

    # TODO
    pass


def event_names(lang=None):

    if lang is None:

        return ds.pull_data('https://api.guildwars2.com/v1/event_names')

    return ds.pull_data('https://api.guildwars2.com/v1/event_names?lang=' + str(lang))


def map_names(lang=None):

    if lang is None:

        return ds.pull_data('https://api.guildwars2.com/v1/map_names')

    return ds.pull_data('https://api.guildwars2.com/v1/map_names?lang=' + str(lang))


def world_names(lang=None):

    if lang is None:

        return ds.pull_data('https://api.guildwars2.com/v1/world_names')

    return ds.pull_data('https://api.guildwars2.com/v1/world_names?lang=' + str(lang))


def event_details(event_id=None, lang=None):

    query = '?='

    if event_id is not None:

        query += str(event_id)

    if lang is not None:

        query += str('&lang=' + lang)

    return ds.pull_data('https://api.guildwars2.com/v1/event_details' + query)

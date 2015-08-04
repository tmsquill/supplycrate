__author__ = 'Zivia'

import supplycrate.dataservice as ds


def wvw_matches():

    return ds.pull_data('https://api.guildwars2.com/v1/wvw/matches')


def wvw_match_details(match_id=None):

    if match_id is not None:

        return ds.pull_data('https://api.guildwars2.com/v1/wvw/match_details?match_id=' + str(match_id))


def wvw_objective_names():

    return ds.pull_data('https://api.guildwars2.com/v1/wvw/objective_names')

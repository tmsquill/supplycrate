__author__ = 'Zivia'

import supplycrate.dataservice as ds


def account(access_token=None):

    return ds.pull_data('https://api.guildwars2.com/v2/account?access_token=' + str(access_token))


def account_bank(access_token=None):

    return ds.pull_data('https://api.guildwars2.com/v2/account/bank?access_token=' + str(access_token))


def account_materials(access_token=None):

    return ds.pull_data('https://api.guildwars2.com/v2/account/materials?access_token=' + str(access_token))


def characters(access_token=None):

    return ds.pull_data('https://api.guildwars2.com/v2/characters?access_token=' + str(access_token))


def commerce_transactions(access_token=None, second_level_endpoint=None, third_level_endpoint=None):

    request = 'https://api.guildwars2.com/v2/commerce/transactions'

    if second_level_endpoint:

        request += '/' + str(second_level_endpoint)

    if third_level_endpoint:

        request += '/' + str(third_level_endpoint)

    if access_token:

        request += '?access_token=' + str(access_token)

    return ds.pull_data(request)


def tokeninfo(access_token=None):

    return ds.pull_data('https://api.guildwars2.com/v2/tokeninfo?access_token=' + str(access_token))

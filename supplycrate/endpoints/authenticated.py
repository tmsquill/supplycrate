__author__ = 'Zivia'

import supplycrate.dataservice as ds


def account(access_token=None):

    if access_token is None:

        # TODO
        pass

    else:

        return ds.pull_data('https://api.guildwars2.com/v2/account?access_token=' + str(access_token))


def account_bank(access_token=None):

    if access_token is None:

        # TODO
        pass

    else:

        return ds.pull_data('https://api.guildwars2.com/v2/account/bank?access_token=' + str(access_token))


def account_materials(access_token=None):

    if access_token is None:

        # TODO
        pass

    else:

        return ds.pull_data('https://api.guildwars2.com/v2/account/materials?access_token=' + str(access_token))


def characters(access_token=None):

    if access_token is None:

        # TODO
        pass

    else:

        return ds.pull_data('https://api.guildwars2.com/v2/characters?access_token=' + str(access_token))


def commerce_transactions(access_token=None):

    # TODO
    pass


def tokeninfo(access_token=None):

    if access_token is None:

        # TODO
        pass

    else:

        return ds.pull_data('https://api.guildwars2.com/v2/tokeninfo?access_token=' + str(access_token))

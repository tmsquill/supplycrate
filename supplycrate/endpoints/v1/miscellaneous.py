__author__ = 'Zivia'

import supplycrate.dataservice as ds


def build():

    return ds.pull_data('https://api.guildwars2.com/v1/build')


def colors():

    return ds.pull_data('https://api.guildwars2.com/v1/colors')


def files():

    return ds.pull_data('https://api.guildwars2.com/v1/files')

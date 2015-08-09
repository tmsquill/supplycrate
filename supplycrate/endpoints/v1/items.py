__author__ = 'Zivia'

import supplycrate.dataservice as ds


def items():

    return ds.pull_data('https://api.guildwars2.com/v1/items')


def item_details(item_id=None, lang=None):

    return ds.pull_data('https://api.guildwars2.com/v1/item_details?item_id=' + str(item_id))


def recipes():

    return ds.pull_data('https://api.guildwars2.com/v1/recipes')


def recipe_details(recipe_id=None, lang=None):

    return ds.pull_data('https://api.guildwars2.com/v1/recipe_details?recipe_id=' + str(recipe_id))


def skins():

    return ds.pull_data('https://api.guildwars2.com/v1/skins')


def skin_details(skin_id=None, lang=None):

    return ds.pull_data('https://api.guildwars2.com/v1/skin_details?skin_id=' + str(skin_id))

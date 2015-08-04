__author__ = 'Zivia'

import supplycrate.dataservice as ds


def guild_details(guild_id=None, guild_name=None):

    if guild_id is not None:

        return ds.pull_data('https://api.guildwars2.com/v1/guild_details.json?guild_id=' + guild_id)

    if guild_name is not None:

        return ds.pull_data('https://api.guildwars2.com/v1/guild_details.json?guild_name=' + guild_name)

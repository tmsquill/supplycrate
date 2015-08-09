__author__ = 'Zivia'

import supplycrate.endpoints.v1.dynamicevents as de
import supplycrate.endpoints.v1.guilds as g
import supplycrate.endpoints.v1.items as it
import supplycrate.endpoints.v1.mapinformation as mi
import supplycrate.endpoints.v1.worldvsworld as wvw
import supplycrate.endpoints.v1.miscellaneous as misc


class TestDynamicEvents:

    def test_event_names(self):

        valid = {u'id', u'name'}
        assert all([set(x.keys()).issubset(valid) for x in de.event_names()])

    def test_map_names(self):

        valid = {u'id', u'name'}
        assert all([set(x.keys()).issubset(valid) for x in de.map_names()])

    def test_world_names(self):

        valid = {u'id', u'name'}
        assert all([set(x.keys()).issubset(valid) for x in de.world_names()])

    def test_event_details(self):

        response = de.event_details()

        valid = {u'events'}
        assert set(response.keys()).issubset(valid)

        valid = {u'name', u'level', u'map_id', u'flags', u'location'}
        assert all([set(response[u'events'][event].keys()).issubset(valid) for event in response[u'events'].keys()])


class TestGuilds:

    def test_guild_details(self):

        response = g.guild_details(guild_name='Opposing All Odds We')

        valid = {u'guild_id', u'guild_name', u'tag', u'emblem'}
        assert set(response.keys()).issubset(valid)

        response = g.guild_details(guild_id='7CA11607-C366-48EC-B4B5-C50E6567FF37')

        valid = {u'guild_id', u'guild_name', u'tag', u'emblem'}
        assert set(response.keys()).issubset(valid)


class TestItems:

    def test_items(self):

        response = it.items()

        valid = {u'items'}
        assert set(response.keys()).issubset(valid)
        assert all([isinstance(x, int) for x in response[u'items']])

    def test_item_details(self):

        response = it.item_details(38875)

        valid = {u'item_id', u'name', u'description', u'type', u'level', u'rarity', u'vendor_value', u'icon_file_id',
                 u'icon_file_signature', u'default_skin', u'game_types', u'flags', u'restrictions', u'armor', u'back',
                 u'bag', u'consumable', u'container', u'gathering', u'gizmo', u'tool', u'trinket',
                 u'upgrade_component', u'weapon'}
        assert set(response.keys()).issubset(valid)

    def test_recipes(self):

        response = it.recipes()

        valid = {u'recipes'}
        assert set(response.keys()).issubset(valid)
        assert all([isinstance(x, int) for x in response[u'recipes']])

    def test_recipe_details(self):

        response = it.recipe_details(1275)

        valid = {u'recipe_id', u'type', u'output_item_id', u'output_item_count', u'min_rating', u'time_to_craft_ms',
                 u'vendor_value', u'disciplines', u'flags', u'ingredients'}
        assert set(response.keys()).issubset(valid)

    def test_skins(self):

        response = it.skins()

        valid = {u'skins'}
        assert set(response.keys()).issubset(valid)
        assert all([isinstance(x, int) for x in response[u'skins']])

    def test_skin_details(self):

        response = it.skin_details(1350)

        valid = {u'skin_id', u'name', u'type', u'flags', u'restrictions', u'icon_file_id', u'icon_file_signature',
                 u'description', u'armor', u'weapon'}
        assert set(response.keys()).issubset(valid)


class TestMapInformation:

    def test_continents(self):

        response = mi.continents()

        valid = {u'continents'}
        assert set(response.keys()).issubset(valid)

        valid = {u'name', u'continent_dims', u'min_zoom', u'max_zoom', u'floors'}
        assert all([set(response[u'continents'][continent].keys()).issubset(valid) for continent in response[u'continents'].keys()])

    def test_maps(self):

        response = mi.maps(15)

        valid = {u'maps'}
        assert set(response.keys()).issubset(valid)

        valid = {u'map_name', u'min_level', u'max_level', u'default_floor', u'floors', u'region_id', u'region_name',
                 u'continent_id', u'continent_name', u'map_rect', u'continent_rect'}
        assert all([set(response[u'maps'][map].keys()).issubset(valid) for map in response[u'maps'].keys()])

    def test_map_floor(self):

        response = mi.map_floor(continent_id=1, floor=1)

        valid = {u'texture_dims', u'clamped_view', u'regions'}
        assert set(response.keys()).issubset(valid)


class TestWorldVsWorld:

    def test_wvw_matches(self):

        response = wvw.wvw_matches()

        valid = {u'wvw_matches'}
        assert set(response.keys()).issubset(valid)

        valid = {u'wvw_match_id', u'red_world_id', u'blue_world_id', u'green_world_id', u'start_time', u'end_time'}
        assert all([set(match.keys()).issubset(valid) for match in response['wvw_matches']])

    def test_wvw_match_details(self):

        response = wvw.wvw_match_details('1-4')

        valid = {u'match_id', u'scores', u'maps'}
        assert set(response.keys()).issubset(valid)

    def test_wvw_objective_names(self):

        response = wvw.wvw_objective_names()

        valid = {u'id', u'name'}
        assert all([set(objective.keys()).issubset(valid) for objective in response])


class TestMiscellaneous:

    def test_build(self):

        response = misc.build()

        valid = {u'build_id'}
        assert set(response.keys()).issubset(valid)

    def test_colors(self):

        response = misc.colors()

        valid = {u'colors'}
        assert set(response.keys()).issubset(valid)

        valid = {u'name', u'base_rgb', u'cloth', u'leather', u'metal'}
        assert all([set(response[u'colors'][color].keys()).issubset(valid) for color in response[u'colors']])

    def test_files(self):

        response = misc.files()

        valid = {u'file_id', u'signature'}
        assert all([set(response[file].keys()).issubset(valid) for file in response.keys()])

__author__ = 'Zivia'

import supplycrate.endpoints.v2.authenticated as auth
import supplycrate.endpoints.v2.items as it
import supplycrate.endpoints.v2.mapinformation as mi
import supplycrate.endpoints.v2.tradingpost as tp
import supplycrate.endpoints.v2.miscellaneous as misc


class TestAuthenticated:

    access_token = 'BEA64142-D54D-EC4B-B6B2-F1E8D66378D096A9E8CB-BCD5-4B74-8E25-6A7DE5ED8C9A'

    access_token_error = {u'text': u'endpoint requires authentication'}

    def test_account(self):

        response = auth.account()
        assert response == self.access_token_error

        response = auth.account(access_token=self.access_token)
        valid = {u'id', u'name', u'world', u'guilds', u'created'}
        assert set(response.keys()).issubset(valid)

    def test_account_bank(self):

        response = auth.account_bank()
        assert response == self.access_token_error

        response = auth.account_bank(access_token=self.access_token)
        valid = {u'id', u'count', u'skin', u'infusions', u'upgrades'}
        assert all([True if x is None or set(x.keys()).issubset(valid) else False for x in response])

    def test_account_materials(self):

        response = auth.account_materials()
        assert response == self.access_token_error

        response = auth.account_materials(access_token=self.access_token)
        valid = {u'id', u'category', u'count'}
        assert all([True if x is None or set(x.keys()).issubset(valid) else False for x in response])

    def test_characters(self):

        response = auth.characters()
        assert response == self.access_token_error

        response = auth.characters(access_token=self.access_token)
        assert all([True if isinstance(x, unicode) else False for x in response])

    def test_commerce_transactions(self):

        response = auth.commerce_transactions()
        assert response == self.access_token_error

        response = auth.commerce_transactions(access_token=self.access_token)
        valid = {u'current', u'history'}
        assert set(response).issubset(valid)

        response = auth.commerce_transactions(second_level_endpoint='current', access_token=self.access_token)
        valid = {u'buys', u'sells'}
        assert set(response).issubset(valid)

        response = auth.commerce_transactions(second_level_endpoint='history', access_token=self.access_token)
        valid = {u'buys', u'sells'}
        assert set(response).issubset(valid)

        response = auth.commerce_transactions(second_level_endpoint='current',
                                              third_level_endpoint='buys',
                                              access_token=self.access_token)
        valid = {u'created', u'price', u'item_id', u'id', u'quantity'}
        assert all([True if x is None or set(x.keys()).issubset(valid) else False for x in response])

        response = auth.commerce_transactions(second_level_endpoint='current',
                                              third_level_endpoint='sells',
                                              access_token=self.access_token)
        valid = {u'created', u'price', u'purchased', u'item_id', u'id', u'quantity'}
        assert all([True if x is None or set(x.keys()).issubset(valid) else False for x in response])

        response = auth.commerce_transactions(second_level_endpoint='history',
                                              third_level_endpoint='buys',
                                              access_token=self.access_token)
        valid = {u'created', u'price', u'purchased', u'item_id', u'id', u'quantity'}
        assert all([True if x is None or set(x.keys()).issubset(valid) else False for x in response])

        response = auth.commerce_transactions(second_level_endpoint='history',
                                              third_level_endpoint='sells',
                                              access_token=self.access_token)
        valid = {u'created', u'price', u'purchased', u'item_id', u'id', u'quantity'}
        assert all([True if x is None or set(x.keys()).issubset(valid) else False for x in response])

    def test_tokeninfo(self):

        response = auth.tokeninfo()
        assert response == self.access_token_error

        response = auth.tokeninfo(access_token=self.access_token)
        valid = {u'id', u'name', u'permissions'}
        assert set(response.keys()).issubset(valid)


class TestItems:

    def test_items(self):

        response = it.items()
        assert all([isinstance(x, int) for x in response])

        response = it.items(it.items())
        valid = {u'id', u'name', u'icon', u'description', u'type', u'rarity', u'level',
                 u'vendor_value', u'default_skin', u'flags', u'game_types', u'restrictions', u'details'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_materials(self):

        response = it.materials()
        assert all(isinstance(x, int) for x in response)

        response = it.materials(it.materials())
        valid = {u'id', u'name', u'items'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_recipes(self):

        response = it.recipes()
        assert all(isinstance(x, int) for x in response)

        response = it.recipes(it.recipes())
        valid = {u'id', u'type', u'output_item_id', u'output_item_count', u'time_to_craft_ms', u'disciplines',
                 u'min_rating', u'flags', u'ingredients'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_recipes_search(self):

        assert all(isinstance(x, int) for x in it.recipes_search(id=46713, input=True))
        assert all(isinstance(x, int) for x in it.recipes_search(id=50065, output=True))

    def test_skins(self):

        response = it.skins()
        assert all(isinstance(x, int) for x in response)

        response = it.skins(it.skins())
        valid = {u'id', u'name', u'type', u'flags', u'restrictions', u'icon', u'description', u'details'}
        assert all([set(x.keys()).issubset(valid) for x in response])


class TestMapInformation:

    def test_continents(self):

        response = mi.continents()
        assert all(isinstance(x, int) for x in response)

        response = mi.continents(mi.continents())
        valid = {u'id', u'name', u'continent_dims', u'min_zoom', u'max_zoom', u'floors'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_maps(self):

        response = mi.maps()
        assert all(isinstance(x, int) for x in response)

        response = mi.maps(mi.maps())
        valid = {u'id', u'name', u'min_level', u'max_level', u'default_floor', u'floors', u'region_id',
                 u'region_name', u'continent_id', u'continent_name', u'map_rect', u'continent_rect'}
        assert all([set(x.keys()).issubset(valid) for x in response])


class TestTradingPost:

    def test_commerce_listings(self):

        response = tp.commerce_listings()
        assert all(isinstance(x, int) for x in response)

        response = tp.commerce_listings(tp.commerce_listings())
        valid = {u'id', u'buys', u'sells'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_commerce_exchange(self):

        valid = {u'coins_per_gem', u'quantity'}
        assert set(tp.commerce_exchange(coins=True, quantity=100000).keys()).issubset(valid)
        assert set(tp.commerce_exchange(gems=True, quantity=100).keys()).issubset(valid)

    def test_commerce_prices(self):

        response = tp.commerce_prices()
        assert all(isinstance(x, int) for x in response)

        response = tp.commerce_prices(tp.commerce_prices())
        valid = {u'id', u'buys', u'sells'}
        assert all([set(x.keys()).issubset(valid) for x in response])


class TestMiscellaneous:

    def test_build(self):

        response = misc.build()
        valid = {u'id'}
        assert set(response.keys()).issubset(valid)

    def test_colors(self):

        response = misc.colors()
        assert all(isinstance(x, int) for x in response)

        response = misc.colors(15)
        valid = {u'id', u'name', u'base_rgb', u'cloth', u'leather', u'metal'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_files(self):

        response = misc.files()
        assert all(isinstance(x, unicode) for x in response)

        response = misc.files('map_complete')
        valid = {u'id', u'icon'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_quaggans(self):

        response = misc.quaggans()
        assert all(isinstance(x, unicode) for x in response)

        response = misc.quaggans('box')
        valid = {u'id', u'url'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_specializations(self):

        response = misc.specializations()
        assert all(isinstance(x, int) for x in response)

        response = misc.specializations(1)
        valid = {u'id', u'name', u'profession', u'elite', u'icon', u'minor_traits', u'major_traits', u'background'}
        assert all([set(x.keys()).issubset(valid) for x in response])

    def test_worlds(self):

        response = misc.worlds()
        assert all(isinstance(x, int) for x in response)

        response = misc.worlds(1001)
        valid = {u'id', u'name'}
        assert all([set(x.keys()).issubset(valid) for x in response])

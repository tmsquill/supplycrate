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

        assert auth.account() == self.access_token_error

        valid = {u'id', u'name', u'world', u'guilds', u'created'}
        result = set(auth.account(access_token=self.access_token).keys()).issubset(valid)

        assert result

    def test_account_bank(self):

        assert auth.account_bank() == self.access_token_error

        valid = {u'id', u'count', u'skin', u'infusions', u'upgrades'}
        result = [True if x is None or set(x.keys()).issubset(valid) else False for x in auth.account_bank(access_token=self.access_token)]

        assert all(result)

    def test_account_materials(self):

        assert auth.account_materials() == self.access_token_error

        valid = {u'id', u'category', u'count'}
        result = [True if x is None or set(x.keys()).issubset(valid) else False for x in auth.account_materials(access_token=self.access_token)]

        assert all(result)

    def test_characters(self):

        assert auth.characters() == self.access_token_error

        result = [True if isinstance(x, unicode) else False for x in auth.characters(access_token=self.access_token)]

        assert all(result)

    def test_commerce_transactions(self):

        assert auth.commerce_transactions() == self.access_token_error

        valid = {u'current', u'history'}
        result = set(auth.commerce_transactions(access_token=self.access_token)).issubset(valid)

        assert result

        valid = {u'buys', u'sells'}
        result = set(auth.commerce_transactions(second_level_endpoint='current',
                                                access_token=self.access_token)).issubset(valid)

        assert result

        valid = {u'buys', u'sells'}
        result = set(auth.commerce_transactions(second_level_endpoint='history',
                                                access_token=self.access_token)).issubset(valid)

        assert result

        valid = {u'created', u'price', u'item_id', u'id', u'quantity'}
        response = auth.commerce_transactions(second_level_endpoint='current',
                                              third_level_endpoint='buys',
                                              access_token=self.access_token)

        result = [True if x is None or set(x.keys()).issubset(valid) else False for x in response]

        assert result

        valid = {u'created', u'price', u'purchased', u'item_id', u'id', u'quantity'}
        response = auth.commerce_transactions(second_level_endpoint='current',
                                              third_level_endpoint='sells',
                                              access_token=self.access_token)

        result = [True if x is None or set(x.keys()).issubset(valid) else False for x in response]

        assert result

        valid = {u'created', u'price', u'purchased', u'item_id', u'id', u'quantity'}
        response = auth.commerce_transactions(second_level_endpoint='history',
                                              third_level_endpoint='buys',
                                              access_token=self.access_token)

        result = [True if x is None or set(x.keys()).issubset(valid) else False for x in response]

        assert result

        valid = {u'created', u'price', u'purchased', u'item_id', u'id', u'quantity'}
        response = auth.commerce_transactions(second_level_endpoint='history',
                                              third_level_endpoint='sells',
                                              access_token=self.access_token)

        result = [True if x is None or set(x.keys()).issubset(valid) else False for x in response]

        assert result

    def test_tokeninfo(self):

        assert auth.tokeninfo() == self.access_token_error

        valid = {u'id', u'name', u'permissions'}
        result = set(auth.tokeninfo(access_token=self.access_token).keys()).issubset(valid)

        assert result


class TestItems:

    def test_items(self):

        assert all([isinstance(x, int) for x in it.items()])

        valid = {u'id', u'name', u'icon', u'description', u'type', u'rarity', u'level',
                 u'vendor_value', u'default_skin', u'flags', u'game_types', u'restrictions', u'details'}
        result = [set(x.keys()).issubset(valid) for x in it.items(it.items())]

        assert all(result)

    def test_materials(self):

        assert all(isinstance(x, int) for x in it.materials())

        valid = {u'id', u'name', u'items'}
        result = [set(x.keys()).issubset(valid) for x in it.materials(it.materials())]

        assert all(result)

    def test_recipes(self):

        assert all(isinstance(x, int) for x in it.recipes())

        valid = {u'id', u'type', u'output_item_id', u'output_item_count', u'time_to_craft_ms', u'disciplines',
                 u'min_rating', u'flags', u'ingredients'}
        result = [set(x.keys()).issubset(valid) for x in it.recipes(it.recipes())]

        assert all(result)

    def test_recipes_search(self):

        assert all(isinstance(x, int) for x in it.recipes_search(id=46713, input=True))
        assert all(isinstance(x, int) for x in it.recipes_search(id=50065, output=True))

    def test_skins(self):

        assert all(isinstance(x, int) for x in it.skins())

        valid = {u'id', u'name', u'type', u'flags', u'restrictions', u'icon', u'description', u'details'}
        result = [set(x.keys()).issubset(valid) for x in it.skins(it.skins())]

        assert all(result)


class TestMapInformation:

    def test_continents(self):

        assert all(isinstance(x, int) for x in mi.continents())

        valid = {u'id', u'name', u'continent_dims', u'min_zoom', u'max_zoom', u'floors'}
        result = [set(x.keys()).issubset(valid) for x in mi.continents(mi.continents())]

        assert all(result)

    def test_maps(self):

        assert all(isinstance(x, int) for x in mi.maps())

        valid = {u'id', u'name', u'min_level', u'max_level', u'default_floor', u'floors', u'region_id',
                 u'region_name', u'continent_id', u'continent_name', u'map_rect', u'continent_rect'}
        result = [set(x.keys()).issubset(valid) for x in mi.maps(mi.maps())]

        assert all(result)


class TestTradingPost:

    def test_commerce_listings(self):

        assert all(isinstance(x, int) for x in tp.commerce_listings())

        valid = {u'id', u'buys', u'sells'}
        assert all([set(x.keys()).issubset(valid) for x in tp.commerce_listings(24)])

    def test_commerce_exchange(self):

        valid = {u'coins_per_gem', u'quantity'}
        assert set(tp.commerce_exchange(coins=True, quantity=100000).keys()).issubset(valid)
        assert set(tp.commerce_exchange(gems=True, quantity=100).keys()).issubset(valid)

    def test_commerce_prices(self):

        assert all(isinstance(x, int) for x in tp.commerce_prices())

        valid = {u'id', u'buys', u'sells'}
        assert all([set(x.keys()).issubset(valid) for x in tp.commerce_prices(24)])


class TestMiscellaneous:

    def test_build(self):

        valid = {u'id'}
        assert set(misc.build().keys()).issubset(valid)

    def test_colors(self):

        assert all(isinstance(x, int) for x in misc.colors())

        valid = {u'id', u'name', u'base_rgb', u'cloth', u'leather', u'metal'}
        result = [set(x.keys()).issubset(valid) for x in misc.colors(15)]

        assert all(result)

    def test_files(self):

        assert all(isinstance(x, unicode) for x in misc.files())

        valid = {u'id', u'icon'}
        result = [set(x.keys()).issubset(valid) for x in misc.files('map_complete')]

        assert all(result)

    def test_quaggans(self):

        assert all(isinstance(x, unicode) for x in misc.quaggans())

        valid = {u'id', u'url'}
        result = [set(x.keys()).issubset(valid) for x in misc.quaggans('box')]

        assert all(result)

    def test_specializations(self):

        assert all(isinstance(x, int) for x in misc.specializations())

        valid = {u'id', u'name', u'profession', u'elite', u'icon', u'minor_traits', u'major_traits', u'background'}
        result = [set(x.keys()).issubset(valid) for x in misc.specializations(1)]

        assert all(result)

    def test_worlds(self):

        assert all(isinstance(x, int) for x in misc.worlds())

        valid = {u'id', u'name'}
        result = [set(x.keys()).issubset(valid) for x in misc.worlds(1001)]

        assert all(result)
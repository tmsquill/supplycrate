__author__ = 'Zivia'

import items as it
import tradingpost as tp

if __name__ == "__main__":

    print 'Trading Post -> Commerce -> Exchange'

    tp.commerce_exchange(coins=True, gems=True, quantity=100000)

    print 'Trading Post -> Commerce -> Listings'

    tp.commerce_listings(ids=[75, 97])

    print 'Trading Post -> Commerce -> Prices'

    tp.commerce_prices(ids=[75, 97])

    print 'Items -> Items'

    it.items(ids=[75, 97])

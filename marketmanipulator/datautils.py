__author__ = 'Zivia'

def chunks(list, n):

    for i in xrange(0, len(list), n):

        yield list[i:i+n]


def format_coin(coin=None):

    copper = coin % 100

    silver = (coin % 10000) / 100

    gold = (coin % 1000000) / 10000

    return str(gold) + 'g ' + str(silver) + 's ' + str(copper) + 'c'
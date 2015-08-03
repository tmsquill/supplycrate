__author__ = 'Zivia'

import sys

def chunks(list, n):

    for i in xrange(0, len(list), n):

        yield list[i:i+n]


def print_update_progress(entity=None, cur=None, max=None):

    sys.stdout.write("\rUpdating " + entity + ": %d%%" % int(100 * float(cur) / max))
    sys.stdout.flush()


def format_coin(coin=None):

    copper = coin % 100

    silver = (coin % 10000) / 100

    gold = (coin % 1000000) / 10000

    return str(gold) + 'g ' + str(silver) + 's ' + str(copper) + 'c'
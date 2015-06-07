__author__ = 'Zivia'


def chunks(list, n):

    for i in xrange(0, len(list), n):

        yield list[i:i+n]

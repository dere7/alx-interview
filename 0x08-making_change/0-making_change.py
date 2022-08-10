#!/usr/bin/python3
''' contains a func that calculates min coins needed
    to make a change'''


def makeChange(coins, total):
    ''' Determine the fewest number of coins needed to
        meet a given amount total for given pile of coins
    '''
    if total <= 0:
        return 0

    number_of_coins = 0
    for coin in sorted(coins, reverse=True):
        if total == 0:
            return number_of_coins
        number_of_coins += total // coin
        total %= coin

    if total == 0:
        return number_of_coins
    return -1

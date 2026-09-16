import numpy as np


# update/add code below ...

def ways(cents, coin_types=[1, 5]):
    counts = [1] + [0] * cents
    for coin in coin_types:
        for amount in range(coin, cents + 1):
            counts[amount] += counts[amount - coin]
    return counts[cents]

def lowest_score(names, scores):
    return names[np.argmin(scores)]

def sort_names(names, scores):
    order = np.argsort(scores)[::-1]
    return list(names[order])
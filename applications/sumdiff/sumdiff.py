"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

from itertools import combinations, permutations

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

def sumdiff(q):
    
    cache_fx = {}

    for i in q:
        cache_fx[i] = f(i)

    cache_sums = {}
    
    for pair in list(combinations(cache_fx.values(), 2)):
        cache_sums[(pair[0], pair[1])] = sum(pair)

    cache_diffs = {}

    for pair in list(permutations(cache_fx.values(), 2)):
        cache_diffs[(pair[0], pair[1])] = pair[0] - pair[1]

    print(cache_fx)
    print(cache_sums)
    print(cache_diffs)

    for key_sum, value_sum in cache_sums.items():
        if value_sum in cache_diffs.values() and value_sum != None:
            print(value_sum)
         

print(sumdiff(q))
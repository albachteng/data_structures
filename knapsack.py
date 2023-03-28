from math import inf


# items will be (weight, value) tuples
def knapsack(items, k, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if (i, k) in lookup:
        return lookup[(i, k)]
    # end of items, return 0
    if i == len(items):
        return 0
    # overshot, do not choose
    elif k < 0:
        return float(-inf)
    # return the max of either taking the value, or leaving the value
    else:
        val = max(
            items[i][1] + knapsack(items, k - items[i][0], i + 1, lookup),
            knapsack(items, k, i + 1, lookup),
        )

        lookup[(i, k)] = val
        return val


items = [(5, 2), (3, 4), (11, 12)]

print(knapsack(items, 10))

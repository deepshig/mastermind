from itertools import combinations


def __heap_permutation(a, size, n, collection):
    if (size == 1):
        collection.append(a)
        return

    for i in range(size):
        __heap_permutation(a, size-1, n, collection)
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]


def generate_all_permutations(a):
    n = len(a)
    collection = []
    __heap_permutation(a, n, n, collection)
    return collection


def generate_all_combinations(a, n):
    if n > len(a):
        return []

    return list(combinations(a, n))

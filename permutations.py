from itertools import combinations
import copy


def __add_permutation(a, collection):
    permutation = copy.deepcopy(a)
    collection.append(permutation)
    return collection


def __heap_permutation(a, size, n, collection):
    if (size == 1):
        collection = __add_permutation(a, collection)
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

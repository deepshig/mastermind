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
    """
    Generate all possible combinations of a list
    of a numbers, using all of them, with no
    repetitions.
    """
    n = len(a)
    collection = []
    __heap_permutation(a, n, n, collection)
    return collection


def generate_all_combinations(a, n):
    """
    Generate all possible combinations of length n
    from a list of a numbers
    """
    if n > len(a):
        return []

    return list(combinations(a, n))


def solver(in_set, k):
    from itertools import combinations
    # Returns the size of a maximal subset if in_set where sum of any 2 numbers is not divisible by k.
    # k : Divisor, 1 <= k <= 100

    n_subsets = lambda n, inp_set: combinations(in_set, n)

    in_set = set(in_set)

    valid_lists = [] # List[Tuple] Satifying all constraints

    max_len = None

    for size in range(2, len(in_set) + 1):
        for candidate in n_subsets(size, in_set):
            # Check if all 2-combination sum is not divisible by k.
            if all([(sum(tup) % k != 0) for tup in combinations(candidate, 2)]):
                # valid_lists.append(candidate)
                temp_len = len(candidate)
                if max_len is None:
                    max_len = temp_len
                else:
                    max_len = temp_len if temp_len > max_len else max_len

    return max_len
    # return max(list(map(len, valid_lists)))

def main():
    ls = {19,10,12,10,24,25,22}
    result = solver(ls, 4)
    print(result)

main()

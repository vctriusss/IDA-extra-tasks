from typing import Callable, Iterable

# Task 1. Palindrome check
tests = [
    'A nut for a jar of tuna.',
    'Borrow or rob?',
    'Was it a car or a cat I saw?',
    '''Dennis, Nell, Edna, Leon, Nedra, Anita,
    Rolf, Nora, Alice, Carol, Leo, Jane, Reed,
    Dena, Dale, Basil, Rae, Penny, Lana, Dave,
    Denny, Lena, Ida, Bernadette, Ben, Ray, Lila,
    Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina,
    Lily, Arne, Bette, Dan, Reba, Diane, Lynn,
    Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned,
    Dee, Rena, Joel, Lora, Cecil, Aaron, Flora,
    Tina, Arden, Noel, and Ellen sinned.''',
    'Murder for a jar of red rum.'
]


def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i != j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def check_tests(pal_func: Callable[[str], bool], tests: Iterable[str]) -> list:
    result = []
    for index, test in enumerate(tests):
        is_or_not = 'is' if pal_func(test) else 'not'
        result.append(f'{index}: {is_or_not} palindrome')
    return result


print(check_tests(is_palindrome, tests))

# Task 2. Two numbers with summ N


def bin_search(arr: list, goal: int) -> int:
    if arr == []:
        return -1
    l, r = 0, len(arr) - 1
    while r - l > 1:
        mid = (l + r) // 2
        if arr[mid] < goal:
            l = mid + 1
        else:
            r = mid

    if arr[l] == goal:
        return l
    if arr[r] == goal:
        return r
    return -1


def check_sum2(arr: list, N: int) -> list:
    pairs = []
    for i, el in enumerate(arr):
        needed = N - el
        ind = bin_search(arr[i+1:], needed)
        if ind != -1:
            pairs.append((el, arr[ind + i + 1]))
    return pairs


def check_sum2_optimized(arr: list, N: int) -> list:
    l, r = 0, len(arr) - 1
    pairs = []
    while l != r:
        s = arr[l] + arr[r]
        if s == N:
            pairs.append((arr[l], arr[r]))
            l += 1
        elif s < N:
            l += 1
        else:
            r -= 1
    return pairs

assert check_sum2_optimized([0, 1, 2, 3, 4, 5, 6, 7], 7) == check_sum2([0, 1, 2, 3, 4, 5, 6, 7], 7) == [(0, 7), (1, 6), (2, 5), (3, 4)]

# Task 3. Three numbers with summ N


def check_sum3(arr: list, N: int) -> list:
    triplets = []
    triplet_sets = set()
    for i, el1 in enumerate(arr):
        for j, el2 in enumerate(arr[i:]):
            if i == j:
                continue
            needed = N - el1 - el2
            less, more = i if i < j else j, j if i < j else i
            slc = arr[:less] + arr[less + 1: more] + arr[more + 1:]
            ind = bin_search(slc, needed)
            if ind != -1:
                needed_ind_add = 0 if ind < less else 1 if less < ind + 1 < more else 2
                triplet = (el1, el2, arr[ind + needed_ind_add])
                if tuple(set(triplet)) not in triplet_sets:  # making unique triplets (optional)
                    triplets.append(triplet)
                    triplet_sets.add(tuple(set(triplet)))
    return triplets


print(check_sum3([0, 1, 2, 3, 4, 5, 6, 7], 8))

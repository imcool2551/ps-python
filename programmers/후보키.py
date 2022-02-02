from itertools import combinations


def is_minimal(key_sets, candidate):
    for key_set in key_sets:
        if set(candidate).issuperset(set(key_set)):
            return False
    return True


def solution(relation):
    row_size = len(relation)  # 6
    col_size = len(relation[0])  # 4

    candidates = []  # 가능한 모든 키 조합
    for i in range(1, col_size + 1):
        candidates.extend(combinations(range(col_size), i))

    print(candidates)
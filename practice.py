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
        candidates.extend(list(combinations(range(col_size), i)))

    key_sets = []
    for candidate in candidates:
        row_sets = set()
        for row in relation:
            row_string = ""
            for idx, col in enumerate(row):
                if idx in candidate:
                    row_string = row_string + col + ','
            row_sets.add(row_string)
        if len(row_sets) == row_size and is_minimal(key_sets, candidate):
            key_sets.append(candidate)

    return len(key_sets)
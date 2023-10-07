from typing import List


def list_avg(seq: List) -> float:
    return sum(seq) / len(seq)


print(list_avg([1,2,4,5,3,9]))



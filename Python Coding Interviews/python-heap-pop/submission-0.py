import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    exit_elem = []
    for i in range(len(heap)):
        exit_elem.append(heapq.heappop(heap))
    return exit_elem


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))

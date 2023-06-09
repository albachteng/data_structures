from typing import Callable, Dict, Generic, List, TypedDict, TypeVar

T = TypeVar("T")


class Heap(Generic[T]):
    heap: List[T] = []
    _lt: Callable[[T, T], bool]

    def __init__(self, val: List[T], fn: Callable[[T, T], bool]) -> None:
        if val is not None:
            self.heap = val
            self._lt = fn
            self.build()

    def swap(self, i: int, j: int) -> None:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def set_lt(self, fn: Callable[[T, T], bool]) -> None:
        self._lt = fn
        self._gt = lambda x, y: not self._lt(x, y)

    def insert(self, val) -> None:
        self.heap.append(val)
        self._heap_up(len(self.heap) - 1)

    def get_min(self):
        if self.heap[0] is not None:
            return self.heap[0]
        else:
            return -1

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        min = self.heap[0]
        self.swap(0, -1)
        self.heap.pop()
        self._heap_down(0)
        return min

    def _heap_up(self, i) -> None:
        parent = (i - 1) // 2
        while i != 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i - 1) // 2

    def _heap_down(self, i) -> None:
        left = 2 * i + 1
        right = 2 * i + 2
        while (
            left < len(self.heap) and not self._lt(self.heap[i], self.heap[left])
        ) or (right < len(self.heap) and not self._lt(self.heap[i], self.heap[right])):
            smallest = (
                left
                if (
                    right >= len(self.heap)
                    or self._lt(self.heap[left], self.heap[right])
                )
                else right
            )
            self.swap(smallest, i)
            i = smallest
            left = 2 * i + 1
            right = 2 * i + 2

    def update_by_index(self, i: int, new) -> None:
        old = self.heap[i]
        self.heap[i] = new
        if new < old:
            self._heap_up(i)
        else:
            self._heap_down(i)

    def update(self, old: T, new: T):
        if old in self.heap:
            self.update_by_index(self.heap.index(old), new)

    def build(self) -> None:
        # self.heap = arr.copy()
        for i in range(len(self.heap))[::-1]:
            self._heap_down(i)


def heap_sort(arr: List[T], fn: Callable[[T, T], bool]) -> List:
    out = []
    h = Heap(arr, fn)
    while len(h.heap):
        out.append(h.extract_min())
    return out


class PriorityQueue:
    def __init__(self, val, fn):
        self.queue = Heap(val, fn)

    def enqueue(self, val):
        self.queue.insert(val)

    def dequeue(self):
        return self.queue.extract_min()

    def peek(self):
        return self.queue.get_min()

    def change_priority_by_index(self, i, new):
        self.queue.update_by_index(i, new)

    def change_priority(self, old, new):
        self.queue.update(old, new)

    def is_empty(self):
        return len(self.queue.heap) == 0


test_arr = [4, 5, 3, 1, 2, 7, 6]


K = TypedDict("K", {"name": str, "count": int})

test_arr_2: List[K] = [
    {"name": "a", "count": 1},
    {"name": "b", "count": 4},
    {"name": "c", "count": 5},
    {"name": "d", "count": 3},
    {"name": "e", "count": 2},
]
# print(heap_sort(test_arr_2, lambda x, y: x["count"] < y["count"]))
print(heap_sort(test_arr_2, lambda x, y: x["name"] < y["name"]))
# test = Heap(test_arr, lambda x, y: x < y)
# print(test.get_min())
# test.update(3, 10)
# print(test.heap)
# test.insert(3)
# print(test.heap)
# print(test.extract_min())
# print(test.extract_min())
# while len(test.heap):
#     x = test.extract_min()
#     print(x)
#     print(test.heap)

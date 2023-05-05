from typing import Generic, List, TypeVar

T = TypeVar("T")


class Heap(Generic[T]):
    heap: List[T] = []

    def __init__(self, *val: T) -> None:
        if val is not None:
            self.heap = [*val]
            self.build()

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
        swap(self.heap, 0, -1)
        self.heap.pop()
        self._heap_down(0)
        return min

    def _heap_up(self, i) -> None:
        parent = (i - 1) // 2
        while i != 0 and self.heap[i] < self.heap[parent]:
            swap(self.heap, i, parent)
            i = parent
            parent = (i - 1) // 2

    def _heap_down(self, i) -> None:
        left = 2 * i + 1
        right = 2 * i + 2
        while (left < len(self.heap) and self.heap[i] > self.heap[left]) or (
            right < len(self.heap) and self.heap[i] > self.heap[right]
        ):
            smallest = (
                left
                if (right >= len(self.heap) or self.heap[left] < self.heap[right])
                else right
            )
            swap(self.heap, smallest, i)
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


def swap(arr: List, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def heap_sort(arr: List) -> List:
    out = []
    h = Heap(*arr)
    while len(h.heap):
        out.append(h.extract_min())
    return out


test_arr = [4, 5, 3, 1, 2, 7, 6]
print(heap_sort(test_arr))
# test = Heap(*test_arr)
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
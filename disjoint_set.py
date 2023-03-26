from typing import Generic, List, TypeVar

T = TypeVar("T")

# disjoint set or union-find
# maintains a collection of disjoint sets (sets that have no elements in common)


class DisjointSet(Generic[T]):
    def __init__(self, elems: List[T]) -> None:
        self.elems = elems
        self.parent = {}
        self.size = {}
        self.rank = {}
        for elem in elems:
            self.make_set(elem)

    # create a new set with a single item, its root is itself
    def make_set(self, x: T):
        self.size[x] = 1  # size includes itself
        self.rank[x] = 0  # depth, which may be larger than it actually is
        self.parent[x] = x

    # find the root of a given element
    def find(self, x) -> T:
        if self.parent[x] == x:
            return x
        else:  # link node directly to its root, potentially lowering rank
            # unfortunately, there doesn't seem to be a way to know for sure
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    # merge two disjoint sets, unless they are part of the same set
    def union(self, x, y) -> None:
        root_x = self.find(x)
        root_y = self.find(y)

        size_x = self.size[root_x]
        size_y = self.size[root_y]

        rank_x = self.rank[root_x]
        rank_y = self.rank[root_y]

        if root_x == root_y:  # already in union
            return
        elif rank_x < rank_y or size_x < size_y:
            # add lesser rank to greater, alternatively add smaller to greater
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            if rank_x == rank_y:
                self.rank[root_y] += 1
            return
        elif rank_y < rank_x or size_y < size_x:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            if rank_x == rank_y:
                self.rank[root_x] += 1
            return
        else:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
            self.rank[root_y] += 1


#
# test = DisjointSet(["A", "B", "C", "D", "E", "F", "G"])
# print(test.parent, test.size, test.rank)
# test.union("A", "B")
# print(test.parent, test.size, test.rank)
# test.union("B", "D")
# print(test.parent, test.size, test.rank)
# test.union("C", "F")
# print(test.parent, test.size, test.rank)
# test.union("G", "D")
# print(test.parent, test.size, test.rank)
# test.union("F", "C")
# print(test.parent, test.size, test.rank)
# test.union("B", "F")
# print(test.parent, test.size, test.rank)
# test.find("C")
# print(test.parent, test.size, test.rank)

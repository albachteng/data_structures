from random import randint

from disjoint_set import DisjointSet


class AdjacencyMatrix:
    def __init__(self, size) -> None:
        self.size = size
        self.board = [[0] * size for _ in range(size)]
        self.cells = [(i, j) for i in range(size) for j in range(size)]

        self.top_island = (-1, 0)
        self.bottom_island = (size, 0)
        self.left_island = (0, -1)
        self.right_island = (0, size)

        self.red = DisjointSet(self.cells + [self.top_island, self.bottom_island])
        self.blue = DisjointSet(self.cells + [self.left_island, self.right_island])
        for i in range(size):
            self.red.union((0, i), self.top_island)
            self.red.union((size - 1, i), self.bottom_island)
            self.blue.union((i, 0), self.left_island)
            self.blue.union((i, size - 1), self.right_island)

    def play(self, i, j, player):
        # assert 0 <= i < self.size and 0 <= i < self.size and self.board[i][j] == 0
        code = 1 if player == "red" else 2
        self.board[i][j] = code
        for nei_i, nei_j in [
            (i + 1, j),
            (i + 1, j - 1),
            (i, j + 1),
            (i, j - 1),
            (i - 1, j),
            (i - 1, j + 1),
        ]:
            if (
                0 <= nei_i < self.size
                and 0 <= nei_j < self.size
                and code == self.board[nei_i][nei_j]
            ):
                if player == "red":
                    self.red.union((nei_i, nei_j), (i, j))
                else:
                    self.blue.union((nei_i, nei_j), (i, j))
        if self.red.find(self.top_island) == self.red.find(self.bottom_island):
            print("red won")
        elif self.blue.find(self.left_island) == self.blue.find(self.right_island):
            print("blue won")


# class Cell:
#     def __init__(self, x, y) -> None:
#         self.x, self.y = x, y
#
#     def topLeft(self) -> Tuple[int, int]:
#         return self.x - 1, self.y
#
#     def topRight(self) -> Tuple[int, int]:
#         return self.x - 1, self.y + 1
#
#     def left(self) -> Tuple[int, int]:
#         return self.x, self.y - 1
#
#     def right(self) -> Tuple[int, int]:
#         return self.x, self.y + 1
#
#     def bottomLeft(self) -> Tuple[int, int]:
#         return self.x + 1, self.y - 1
#
#     def bottomRight(self) -> Tuple[int, int]:
#         return self.x + 1, self.y + 1
#

test = AdjacencyMatrix(5)
# for cell in test.cells:
#     x, y = cell
#     print(x, y)

# for set in test.red.elems:
#     x, y = set
#     print(x, y)

for _ in range(5):
    player = "blue"
    for _ in range(5):
        x, y = randint(0, 4), randint(0, 4)
        test.play(x, y, player)
        player = "blue" if player == "red" else "red"

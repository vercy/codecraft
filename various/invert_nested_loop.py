

# inverting nested loops
list_of_lists = [
    [1, 1, 2, 3],
    [4, 5, 5],
    [6, 8, 9],
    [10]
]


class ListOfListIterator:
    def __init__(self, lol):
        self.lol = lol
        self.i = 0
        self.j = 0

    def has_next(self):
        while self.i < len(self.lol):
            while self.j < len(self.lol[self.i]):
                if self.lol[self.i][self.j] % 2 == 0:
                    return True
                else:
                    self.j += 1
            self.j = 0
            self.i += 1
        return False

    def next(self):
        res = self.lol[self.i][self.j]
        self.j += 1
        return res


# it = ListOfListIterator(list_of_lists)
# while it.has_next():
#     print(it.next())


def it_lol(lol):
    for inner_list in lol:
        for element in inner_list:
            if element % 2 == 0:
                yield element


for even in it_lol(list_of_lists):
    print(even)

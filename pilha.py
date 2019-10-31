import random, string

class Node(object):
    """docstring for Node."""

    def __init__(self, node):
        self.data = node
        self.next = None


class Pilha(object):
    """docstring for Pilha."""

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        self.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self, elem):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self.size - 1
            return node
        print("A pilha esta vazia")

    def peek(self):
        return self.top.self.data

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

if __name__ == '__main__':
    pilha = Pilha()
    o = 0
    for i in range(1000):
        palavra = o
        n = Node(palavra)
        print(n.data)
        pilha.push(n)
        o = o + 1

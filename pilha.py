# -*- coding: utf-8 -*-
import random, string

class Node(object):
    """docstring for Node."""

    def __init__(self, node):
        self.data = node
        self.next = None

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return self.__repr__()

class Pilha(object):
    """docstring for Pilha."""

    def __init__(self):
        self.top = None
        self._size = 0

    def get_size(self):
        return self._size

    def push(self, elem):
        node = Node(elem)
        node.next = self.top
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
        return self.top

    def __repr__(self):
        atual = self.top
        while atual is not None:
            print(atual.next)
            atual = atual.next

        """
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r
        """

    def __str__(self):
        return str(self.__repr__())

if __name__ == '__main__':
    pilha = Pilha()
    o = 0
    for i in range(1000):
        palavra = o
        n = Node(palavra)
        print(n.data)
        pilha.push(n)
        o = o + 1

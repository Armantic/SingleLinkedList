# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.__head = Node(value=None)

    def __str__(self):
        current_node = self.__head.next
        out = ''
        while current_node:
            out += '{} '.format(current_node.value)
            current_node = current_node.next
        return out

    def __findNodeBefore(self, value):
        current_node = self.__head
        while current_node.next:
            if current_node.next.value == value:
                return current_node
            current_node = current_node.next
        return None

    def __findNode(self, value):
        current_node = self.__head.next
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.next
        return None

    def addAtBeginning(self, new_node):
        if new_node:
            new_node.next = self.__head.next
            self.__head.next = new_node

    def addAtEnd(self, new_node):
        tail = self.__head
        if new_node:
            while tail.next:
                tail = tail.next
            new_node.next = tail.next
            tail.next = new_node

    def insertAfter(self, after_value, new_value):
        after_node = self.__findNode(after_value)
        if after_node:
            new_node = Node(new_value)
            new_node.next = after_node.next
            after_node.next = new_node

    def removeNode(self, value):
        after_node = self.__findNodeBefore(value)
        if after_node:
            del_node = after_node.next
            after_node.next = del_node.next
            del del_node
        else:
            raise ValueError('Item: {} not found'.format(value))

    def clear(self):
        while self.__head.next:
            del_node = self.__head.next
            self.__head.next = del_node.next
            del del_node

    def size(self):
        current_node = self.__head.next
        count = 0
        while current_node:
            current_node = current_node.next
            count = count + 1
        return count

    def findMax(self):
        if self.__head.next:
            current_node = self.__head.next
            max_value = current_node.value
            while current_node.next:
                if max_value < current_node.next.value:
                    max_value = current_node.next.value
                current_node = current_node.next
            return max_value
        return None

if __name__ == "__main__":

    list = SingleLinkedList()
    list.addAtBeginning(Node(3))
    list.addAtEnd(Node(6))
    list.addAtEnd(Node(9))
    list.addAtBeginning(Node(10))

    print(list)
    print('Size = {}'.format(list.size()))

    list.removeNode(6)
    print(list)
    print('Size = {}'.format(list.size()))

    list.insertAfter(3, 7)
    list.insertAfter(7, 18)
    print(list)
    print('Size = {}'.format(list.size()))

    print('Max value = {}'.format(list.findMax()))

    list.clear()
    print('Size = {}'.format(list.size()))










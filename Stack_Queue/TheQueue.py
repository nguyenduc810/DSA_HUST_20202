import random as rd


class Node:
    # to init a new Node with given value
    def __init__(self, value):
        self.data = value
        self.next = None


# class Queue to represent the queue of customers waiting
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty() :
            self.head = self.tail = newNode
            self.size += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty.")
            return
        tmp = self.head
        self.head = tmp.next
        self.size -= 1
        return tmp.data

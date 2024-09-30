class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                break
            currentNode = currentNode.next
        currentNode.next = newNode

    def printLL(self):
        if self.head is None:
            print("Empty list")
            return
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is None:
                print(currentNode.data)
            else:
                print(currentNode.data, "=>", end=" ")
            currentNode = currentNode.next

    def countLength(self):
        size = 0
        currentNode = self.head
        while currentNode is not None:
            size += 1
            currentNode = currentNode.next
        return size

    def removeNthNodeFromLast(self, n):
        size = linkedlist.countLength()
        if size < n:
            print("linkedlist Does not contain ", n, "th node")
            return not None  # not None for output format check if for better understanding
        if n == size:
            self.head = self.head.next
            return
        idx = 1
        prevNode = None
        currentNode = self.head
        while currentNode:
            if size - n + 1 == idx:
                if currentNode.next is None:
                    prevNode.next = None
                else:
                    prevNode.next = currentNode.next
            idx += 1
            prevNode = currentNode
            currentNode = currentNode.next


linkedlist = LinkedList()
linkedlist.insert(Node(1))
linkedlist.insert(Node(21))
linkedlist.insert(Node(321))
linkedlist.insert(Node(4321))
linkedlist.insert(Node(54321))
linkedlist.insert(Node(654321))
linkedlist.printLL()
if linkedlist.removeNthNodeFromLast(int(input("Enter nth node you want to delete from last: "))) is None:
    linkedlist.printLL()

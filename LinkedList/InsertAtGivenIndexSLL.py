# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# insert Node at given index
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtGivenIndex(self, idx, newNode):
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while idx != 1:
            if currentNode is None:
                print("Index out of bound so no changes...so ", end="")
                return
            currentNode = currentNode.next
            idx -= 1
        newNode.next = currentNode.next
        currentNode.next = newNode

    # insert element at end
    def insetEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while True:
            if lastNode.next is None:
                break
            lastNode = lastNode.next
        lastNode.next = newNode

    # print ll
    def printLL(self):
        if self.head is None:
            print("Empty List")
            return
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is not None:
                print(currentNode.data, "<=>", end="")
            else:
                print(currentNode.data)
            currentNode = currentNode.next


linkedlist = LinkedList()
linkedlist.insetEnd(Node(12))
linkedlist.insetEnd(Node(12))
linkedlist.insetEnd(Node(2323))
linkedlist.insetEnd(Node(222))
linkedlist.insetEnd(Node(154))
linkedlist.insetEnd(Node(162))
linkedlist.insetEnd(Node(2323))
linkedlist.insetEnd(Node(20))
print("linkedList:")
linkedlist.printLL()
print("Enter index At which you want to insert Element")
index = int(input())
print("Enter value:")
value = int(input())
linkedlist.insertAtGivenIndex(index, Node(value))
print("Updated List:")
linkedlist.printLL()

# create node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create List
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

    # print list
    def printLL(self):
        if self.head is None:
            print("Empty List")
            return
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is not None:
                print(currentNode.data, "=>", end="")
            else:
                print(currentNode.data)
            currentNode = currentNode.next

# remove first element
    def removeFirstElement(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next is None:
            print("List has only one element!")
            return
        self.head = self.head.next


linkedlist = LinkedList()
linkedlist.insert(Node(1))
linkedlist.insert(Node(2))
linkedlist.insert(Node(3))
linkedlist.insert(Node(4))
linkedlist.insert(Node(5))
linkedlist.insert(Node(6))
linkedlist.insert(Node(7))
linkedlist.insert(Node(8))
linkedlist.insert(Node(9))
linkedlist.insert(Node(10))
linkedlist.insert(Node(11))
linkedlist.insert(Node(12))
linkedlist.insert(Node(13))
linkedlist.printLL()
linkedlist.removeFirstElement()

# print list after removing first element

print("After removing first element:")
linkedlist.printLL()


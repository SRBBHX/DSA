# create node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# insert element
class LinkedList:
    def __init__(self):
        self.head  = None

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

# print linkedlist
    def printLL(self):
        if self.head is None:
            print("Empty List")
            return
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is not  None:
                print(currentNode.data, "=>", end="")
            else:
                print(currentNode.data)
            currentNode = currentNode.next

# remove last element
    def removeLastElement(self):
        if self.head is None:
            print("Empty List")
            return
        if self.head.next is None:
            self.head = None
            return
        currentNode = self.head
        while currentNode.next.next is not None:
            currentNode = currentNode.next
        currentNode.next = None
# inserting nodes
linkedlist = LinkedList()
linkedlist.insert(Node(10))
linkedlist.insert(Node(20))
linkedlist.insert(Node(30))
linkedlist.insert(Node(40))
linkedlist.insert(Node(50))
linkedlist.insert(Node(60))
linkedlist.insert(Node(70))
linkedlist.insert(Node(80))
linkedlist.insert(Node(90))
linkedlist.insert(Node(100))
linkedlist.insert(Node(110))
linkedlist.insert(Node(120))
linkedlist.insert(Node(130))
linkedlist.printLL()
linkedlist.removeLastElement()
linkedlist.printLL()

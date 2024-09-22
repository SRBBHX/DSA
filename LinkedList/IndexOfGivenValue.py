# create Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# insert node
class LinkedList:
    index = 0

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

    # return index of given val
    def returnIndex(self, val):
        if self.head is None:
            return
        currentNode = self.head
        while currentNode is not None:
            if currentNode.data == val:
                return self.index
            currentNode = currentNode.next
            self.index += 1

    # print ll
    def printLL(self):
        if self.head is None:
            print("Empty list!")
            return
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is not None:
                print(currentNode.data, "=>", end="")
            else:
                print(currentNode.data)
            currentNode = currentNode.next


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
val = int(input("Enter value: "))
index = linkedlist.returnIndex(val)
if index is None:
    print("Given element is not present in list!")
else:
    print("Given value is present at index:", index)


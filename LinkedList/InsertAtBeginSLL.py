class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        newNode.next = self.head
        self.head = newNode

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


firstNode = Node("Lakshman")
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node("shyam")
linkedlist.insert(secondNode)
thirdNode = Node("Ram")
linkedlist.insert(thirdNode)
linkedlist.printLL()

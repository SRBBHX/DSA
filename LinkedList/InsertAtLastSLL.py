# create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# create ll
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
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
    def printLinkedlist(self):
        if self.head is None:
            print("Empty List")
            return
        currentNode = self.head
        while currentNode is not None:

            if currentNode.next is not None:
                print(currentNode.data, "=>", end=" ")
            else:
                print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node("Ram")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Shyam")
linkedList.insert(secondNode)
thirdNode = Node("Sita")
linkedList.insert(thirdNode)
fourthNode = Node("Lakshmana")
linkedList.insert(fourthNode)
linkedList.printLinkedlist()

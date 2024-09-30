# create Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


# insert Node
class LinkedList:
    def __init__(self) -> None:
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

    # print List
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

    # reverse List
    def revList(self):
        if self.head is None:
            return
        prevNode = None
        currNode = self.head
        while True:
            if currNode.next is None:
                break
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        currNode.next = prevNode
        self.head = currNode


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
linkedlist.revList()
print("Reversed List:-")
linkedlist.printLL()


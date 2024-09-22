# node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# insert element
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        currentNode = self.head
        if currentNode.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
            return
        while currentNode.next.data < new_node.data:
            currentNode = currentNode.next

        else:
            new_node.next = currentNode.next
            currentNode.next = new_node

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


# print element
firstNode = Node(12)
linkedlist = LinkedList()
linkedlist.insert(firstNode)
secondNode = Node(10)
linkedlist.insert(secondNode)
thirdNode = Node(15)
linkedlist.insert(thirdNode)
linkedlist.printLL()

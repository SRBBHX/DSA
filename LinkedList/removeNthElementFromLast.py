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
            print("emptyList", end="")
            return
        currentNode = self.head
        while currentNode is not None:
            if currentNode.next is not None:
                print(currentNode.data, "=>", end="")
            else:
                print(currentNode.data)
            currentNode = currentNode.next

    def reverse(self):
        if self.head is None:
            print("so can't reverse")
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

    def removeNthFromLast(self, node):
        idx = 2
        if node == 1:
            self.head = self.head.next
            return
        currentNode = self.head
        while True:
            if currentNode.next is None:
                if idx < node:
                    return "list is too less"
                break
            if idx == node:
                currentNode.next = currentNode.next.next
                return
            idx += 1
            currentNode = currentNode.next

    def countLength(self):
        length = 0
        if self.head is None:
            return 0
        currentNode = self.head
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length


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
linkedlist.reverse()
linkedlist.removeNthFromLast(int(input("Enter nth element that you want to delete from last: ")))
linkedlist.reverse()
linkedlist.printLL()

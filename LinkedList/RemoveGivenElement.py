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

    def removeGivenElement(self, value):
        if self.head is None:
            return "Empty lsit so no update...."
        if self.head.data == value:
            self.head = self.head.next
            return " updated list...."
        currentNode = self.head
        flag = 0
        while True:
            if currentNode.next is None:
                break
            if currentNode.next.data == value:
                flag +=1
                currentNode.next = currentNode.next.next
                return "updated list...."
            currentNode = currentNode.next
        if flag == 0:
            return "Value is not existing in linkedlist"



    def printLL(self):
        if self.head is None:
            print("emptyList")
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
val = int(input("Enter the value you want to remove:"))
print(linkedlist.removeGivenElement(val))
linkedlist.printLL()
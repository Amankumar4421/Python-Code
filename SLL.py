class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head == None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data," ")
                temp=temp.next
    def insertAtBeg(self,data):
        newNode = Node(data)
        newNode.next=self.head
        self.head=newNode

    def insertAtEnd(self,data):
        newNode = Node(data)
        temp = self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=newNode

    def insertAtPos(self,data,pos):
        newNode = Node(data)
        temp = self.head
        if(pos==1):
            newNode.next=temp
            self.head=newNode
        else:
            for i in range(0,pos-2):
                temp=temp.next
            newNode.next=temp.next
            temp.next=newNode


ll1 = LinkedList()
ll1.insertAtBeg(10)
ll1.insertAtBeg(20)
ll1.insertAtEnd(30)
ll1.insertAtPos(40,4)
ll1.display()
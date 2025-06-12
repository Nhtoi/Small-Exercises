class Node():
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList():
    
    def __init__(self):
        self.head = None
    
    def InsertNode(self, value):
        node = Node(value, self.head)
        self.head = node
    
    def InsertNodeAtEnd(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(value, None)

    def PrintLinkedList(self):
        if self.head is None:
            print("Empty Linked List")
            return
        itr = self.head
        linkedlist = ""
        while itr:
            linkedlist += str(itr.val) + "-->"
            itr = itr.next
        print(linkedlist)
    
    def CreateLinkedListFromArray(self, array):
        # self.head = None
        # for values in array:
        #     self.InsertNode(values)
        self.head = None
        for values in array:
            self.InsertNodeAtEnd(values)
    
    def getlength(self):
        if self.head is None:
            return 0
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def InsertAfterValue(self, value, valueAfter):
        if self.head is None:
            print("List is Empty Cannot Insert After Value")
            return
        itr = self.head

        while itr:
            if itr.val == value:
                node = Node(valueAfter, itr.next)
                itr.next = node
                break
            itr = itr.next

    def RemoveByValue(self, value):
        if self.head is None:
            print("List is Empty Cannot Insert After Value")
            return
        itr = self.head
        while itr:
            if itr.next.val == value:
                itr.next = itr.next.next
                break
            itr = itr.next
        return -1
    
    def DeleteFromList(self, index):
        if index < 0 or index >= self.getlength():
            return print("Cannot Delete Linked List is Empty or Index not in List")
        if index == 0:
            self.head = self.head.next
            return
        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next
                break
            itr = itr.next
            count += 1
            
    def InsertAt(self, index, value):
        if index < 0 or index > self.getlength():
            return print("Cannot Insert Item into Linked List Because it is Empty or Index not in List")
        elif index == 0:
            self.InsertNode(value)
            return
        elif index == self.getlength():
            self.InsertNodeAtEnd(value)
            return
        
        itr = self.head
        count = 0
        
        while itr:
            if count == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        
ll = LinkedList()

ll.CreateLinkedListFromArray([13,5,7,54,3,12,3,5,7,6])

ll.PrintLinkedList()

ll.DeleteFromList(1)

ll.PrintLinkedList()
#index, value
ll.InsertAt(9, 1827)

ll.PrintLinkedList()

ll.InsertAfterValue(7, 123)

ll.PrintLinkedList()

ll.RemoveByValue(12)

ll.PrintLinkedList()
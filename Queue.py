class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def Enqueue(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def Create(self, values):
        for value in values:
            self.Enqueue(value)

    def dequeue(self):
        if self.head is None:
            return -1
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.head is None:
            self.tail = None 
        return value

    def Peek(self):
        return self.head.value if self.head else None

    def Print(self):
        itr = self.head
        string = ""
        while itr:
            string += str(itr.value) + "-->"
            itr = itr.next
        print(string + "None")
        print("Length:", self.length)
        if self.head:
            print("Head:", self.head.value)
        if self.tail:
            print("Tail:", self.tail.value)


queue = Queue()
queue.Create([13, 3, 5, 245, 3, 1, 12])
queue.Print()
print("Peek:", queue.Peek())
print("Dequeued:", queue.dequeue())
queue.Print()
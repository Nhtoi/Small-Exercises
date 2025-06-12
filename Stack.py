class Node():
    def __init__(self, val=None, prev=None):
        self.val = val
        self.prev = prev

class Stack():
    def __init__(self):
        self.head = None
        self.length = 0

    def create(self, array):
        for num in array:
            self.push(num)

    def push(self, number):
        node = Node(number, self.head)
        self.head = node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.prev
        self.length -= 1
        return val

    def peek(self):
        return self.head.val if self.head else None

    def print(self):
        itr = self.head
        if itr is None:
            print("Stack is empty")
            return
        string = ""
        while itr:
            string += str(itr.val) + "-->"
            itr = itr.prev
        print(string)
        print("Length:", self.length)


stack = Stack()
stack.create([123, 6, 5, 4, 4, 123, 1, 5, 6, 8, 75])
stack.print()         
stack.push(2)
stack.print()        
print("Top:", stack.peek()) 
print("Popped:", stack.pop()) 
stack.print()        
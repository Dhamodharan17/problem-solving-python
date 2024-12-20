class Stack:
    # insert and delete with head
    # insert - newNode.next = head
    # delete - head = head.next
    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    #push
    def push(self, x):
        print("Push Operation ",x)
        newNode = self.Node(x)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    #pop
    def pop(self):
        print("Pop Operation")
        if self.head is None:
            print("Empty Stack")
            return
        else:
            print(self.head.data)
            self.head = self.head.next
    #peek
    def peek(self):
        print("Peek Operation")
        if self.head is None:
            print("Empty Stack")
            return
        print(self.head.data)
    
stack1 = Stack()
stack1.push(3)
stack1.push(2)
stack1.pop()
stack1.peek()

        

    


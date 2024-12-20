class Stack:

    size = 0
    data = []
    top = -1

    #constructor
    def __init__(self, size):
        self.size = size
        self.data = [0] * size
    
    #push
    def push(self, x):
        if self.top == self.size - 1:
            print("Stack Full")
            return
        self.top += 1
        self.data[self.top] = x
        
    #pop
    def pop(self):
        if self.top == -1:
            print("Stack Empty")
            return
        #print("poped", self.data[self.top])
        self.top -=1

    #peek
    def peek(self):
        if self.top == -1:
            print("Empty Stack")
            return
        print(self.data[self.top], " at top")
    


#main
stack1 = Stack(3)
stack1.push(0)
stack1.push(1)
stack1.push(2)
stack1.push(3)
#last in 1st out
#stack1.pop()
#stack1.pop()
#stack1.pop()
#stack1.pop()
stack1.peek()
    

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack: # if minStack empty
            self.minStack.append(val)
        else: #if minStack has a value, we compare and update
            self.minStack.append(min(val, self.minStack[-1]))
        

    def pop(self) -> None: #just pop, operations were taken care of by push
        self.minStack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1] #return the end of the array (top)
        

    def getMin(self) -> int:
        return self.minStack[-1] #return the top of minStack(top will always be the min the way we set it up)
        

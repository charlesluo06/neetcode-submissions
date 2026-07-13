class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b = stack.pop() #2nd to last
                a = stack.pop() #last element in stack
                stack.append(a - b) #subtract in correct order
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                b = stack.pop() #2nd to last
                a = stack.pop() #last element in stack
                stack.append(int(a / b)) #divide in correct order and convert so not decimal
            else: #case if number
                stack.append(int(c)) #push to stack, change to number
        return stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        
        #stack[-1] means top of stack, end of list
        for c in s:
            if c in closeToOpen: #case if closing parenthesis
                if stack and stack[-1] == closeToOpen[c]: #if stack exists and is the top of stack == expected match for current closing p
                    stack.pop() #pop the top
                else: #parenthesis don't match
                    return False
            else: #case for opening p
                stack.append(c)
        if not stack:
            return True
        else:
            return False
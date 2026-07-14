class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair : [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #if current t is greater than top of stack, pop top and add to stack
                stackT, stackIndex = stack.pop() # pop top, save popped index
                res[stackIndex] = (i - stackIndex) #update corresponding res index with curr i - popped index
            stack.append([t,i]) #1. if not bigger, append to stack 2. after popping and updating append to stack
        return res #return array
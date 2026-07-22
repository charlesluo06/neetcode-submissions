class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: #height too great
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) #height * width
                start = index
            stack.append((start, h))
        
        for i, h in stack: #heights that lasted til the end we need to go back
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
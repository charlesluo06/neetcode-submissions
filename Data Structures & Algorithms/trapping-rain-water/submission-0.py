class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        # computation: min(l,r) - height[i] = water at i

        while l < r:
            if leftMax < rightMax: # BOTTLENECK
                l += 1
                leftMax = max(leftMax, height[l]) # update if current left ptr is bigger
                res += leftMax - height[l] # compute and add water to res
            else: # BOTTLENECK
                r -= 1
                rightMax = max(rightMax, height[r]) # update if current right ptr is bigger
                res += rightMax - height[r] # compute and add water to res
        return res
            
            


        
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0
        r = 0
        q = collections.deque() #STORES INDICES

        while r < len(nums): #while r in bounds
            while q and nums[q[-1]] < nums[r]:
                q.pop() 
            q.append(r)

            if l > q[0]: #check if left ptr has moved past the left most in deque (expired)
                q.popleft() #update left most q value

            if (r + 1) >= k: #only once window is valid, we add to output and shift left ptr
                output.append(nums[q[0]])
                l+=1
            r+=1 # every iteration we shift right

        return output

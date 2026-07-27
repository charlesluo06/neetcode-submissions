class Solution:
    def findMin(self, nums: List[int]) -> int:

        #BIG IDEA: Rotated Sorted's left will be bigger or smaller than mid

        res = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]: #Base case as res
                res = min(res, nums[l])
                break
            mid = (l + r) // 2
            res = min(res, nums[mid]) #is the left ptr or mid smaller?
            if nums[mid] >= nums[l]:   #if mid bigger or same, shift search to right
                l = mid + 1
            else:                     #else, shift search to right
                r = mid - 1
        return res

        
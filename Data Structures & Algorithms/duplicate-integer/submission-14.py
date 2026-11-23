class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #array of nums
        #if dupe, return false
        #loop thru once, store in a set after each iteration, if element is already in the set, return false
        #after loop is done, return True since no dupes

        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i]) #add to set
        return False
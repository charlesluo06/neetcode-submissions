class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap
        seen = set()
        for i in range(len(nums)): #loop thru each element
            if nums[i] in seen: #if element is already in the set from prev iteration, return true
                return True
            seen.add(nums[i]) #if not, add it to the set
        return False

        
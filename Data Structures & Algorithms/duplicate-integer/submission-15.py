class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #array of nums, return bool depending if there is a dupe in the array

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i]) #adding to set every #
        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the 2 indices that allow e1 + e2 == target, return a pair?
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
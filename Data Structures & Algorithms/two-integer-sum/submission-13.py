class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input: array of nums, target
        #output: the indices of the elements that add up to target
        #ex: target = 7, return indices of 3 + 4.

        seen = {}

        for i,n in enumerate(nums):
            diff = target - n # 7 - 4 = 3
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i #we have val, looking for index
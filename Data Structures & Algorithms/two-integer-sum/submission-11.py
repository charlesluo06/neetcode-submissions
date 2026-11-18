class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #returning the indices from the 2 vals that add up to target
        #1 pass, find diff and compare to see if we have found the diff in our set

        seen = {}

        for i, n in enumerate(nums): #i = index, n = val
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i #store current val in nums

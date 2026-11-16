class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            diff = target - val #find diff for this iteration
            if diff in seen:    #if diff is in the set
                return [seen[diff], i]  #return the index of diff and the current index
            seen[val] = i #updating seen
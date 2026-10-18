class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #return the 2 indices that allow e1 + e2 == target, return a pair?
        #one pass, store in dict every element, as well as check if complement exists in dict
        seen = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in seen: #if compliment in dict, return the indices
                return [seen[compliment], i]
            seen[num] = i #add val to dict



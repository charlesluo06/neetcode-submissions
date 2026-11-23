class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find the elements that add up to target and return their indices
        #store in hashmap, seen[n] = i, enumerate
        #look for diff in the hashmap

        seen = {} #create hashmap seen[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i #match n to indice
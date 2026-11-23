class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #assuming its the same as Two Sum, returning the indice + 1 this time tho
        #return the indices of the elements that add up to target
        #ex: indices of 3 + 4 = 7 (target)

        seen = {}


        for i,n in enumerate(numbers):
            diff = target - n
            if diff in seen:
                return [seen[diff] + 1, i + 1]
            seen[n] = i #have n, looking for indice
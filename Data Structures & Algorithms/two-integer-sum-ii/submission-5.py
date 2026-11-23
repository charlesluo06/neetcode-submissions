class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two ptr approach, ALWAYS VALID SOLUTION
        #1, 2, 3, 4, 5 | target = 3
        #6, 5, 4, 3
        #im thinking if sum is too big, close right, if sum is too small, close left
        #1-indexed



        l = 0
        r = len(numbers) - 1 

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1 , r + 1] #indices (1-indexed)
            if sum < target:
                l+=1
            if sum > target:
                r-=1
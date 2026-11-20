class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input: array of numbers, target sum
        #output: array of 2 indexes that add to the target

        l = 0
        r = len(numbers) - 1
        sum = 0

        #1,2,3,4 --- target = 3

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l+=1
            if sum > target:
                r-=1
            elif sum == target:
                return [l + 1, r + 1]











        return False
            
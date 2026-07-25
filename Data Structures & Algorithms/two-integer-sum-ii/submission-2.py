class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #input: array of numbers, target sum
        #output: array of 2 indexes that add to the target

        l = 0
        r = len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1
            if currSum < target:
                l += 1
            elif currSum == target:
                return [l + 1, r + 1]
        return False


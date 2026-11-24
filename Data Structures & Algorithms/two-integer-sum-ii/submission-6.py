class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two ptrs, find the indices of the elements that add up to target, PTRS ARE THE INDICES
        #sorted already, so if sum is too small, close left, if sum is too big, close right

        l = 0
        r = len(numbers) - 1
        #1, 2, 3, 4

        while l < r:
            sum = numbers[l] + numbers[r] # 1 + 4 = 5
            if sum == target: #found indices
                return [l + 1, r + 1]
            #cases to adjust ptrs
            if sum < target:
                l += 1
            if sum > target:
                r -= 1
        
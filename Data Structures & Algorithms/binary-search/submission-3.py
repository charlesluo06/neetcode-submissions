class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search is splitting the array in half, checking the middle, which decide which half to check

        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return mid
        return -1
        
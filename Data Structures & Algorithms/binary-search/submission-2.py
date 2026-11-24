class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search is splitting it in half, and deciding between the lower and upper half
        #ascending, target

        #split, check target, if lower searc hlower half

        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] == target:
                return mid
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input: ascending array, target
        #output: search for target and return index
        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                return mid
        return -1
            
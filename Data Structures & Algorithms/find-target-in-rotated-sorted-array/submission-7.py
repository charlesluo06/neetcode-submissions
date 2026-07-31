class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: #case if mid is the target
                return mid

            #LEFT PORTION
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: #target is greater than mid
                    l = mid + 1
                else: #target < mid, but greater than l
                    r = mid - 1

            #RIGHT PORTION
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else: #target greater than mid, less than r
                    l = mid + 1

        return -1
            

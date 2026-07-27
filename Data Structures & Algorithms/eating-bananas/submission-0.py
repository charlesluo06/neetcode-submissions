class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r #looking for min

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles: #test k on piles
                 hours += math.ceil(float(p) / k)
            if hours <= h: #if valid k, update min res
                res = min(res, k)
                r = k - 1
            else: # k is not valid hours
                l = k + 1
        return res

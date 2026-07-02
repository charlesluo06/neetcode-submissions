class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buying
        r = 1 # selling
        maxProfit = 0 # default
        
        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r # case for left lower than right
            r+=1
        return maxProfit
        
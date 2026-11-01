class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = float("inf")
        sell = 0
        
        for p in prices:
            buy = min(buy,p)
            sell = max(sell, p-buy)
        
        return sell
        
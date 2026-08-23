class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        sell=0
        for n in prices:
            buy=min(buy,n)
            sell=max(sell,n-buy)
        return sell
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 9999999999
        max_res = 0
        for price in prices:
            m = min(m, price)
            max_res = max(max_res, price - m)
        return max_res
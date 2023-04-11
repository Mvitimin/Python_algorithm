from typing import List

class Solution:
	def maxProfit(self, prices: List[int], fee: int) -> int:
		n = len(prices)
		sell, buy = 0, -prices[0]
		for i in range(n):
			sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
		return sell
			
a = Solution()
prices = [1,3,2,8,4,9]; fee = 2
prices = [1,3,7,5,10,3]; fee = 3
print(a.maxProfit(prices, fee))

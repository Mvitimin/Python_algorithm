from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		buy, sell = -prices[0], 0
		ans = 0
		for i in range(1, len(prices)):
			sell, buy = max(sell, buy + prices[i]), max(buy, sell - prices[i])
		return sell
			
a = Solution()
prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
print(a.maxProfit(prices))

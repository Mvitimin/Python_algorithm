from typing import List
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		reset = 0
		sell = 0 
		buy = -prices[0]
		for i in range(1, n):	
			buy, sell, reset = max(buy, reset - prices[i]), max(sell, buy + prices[i]), sell
		return sell
		
a = Solution()
prices = [1,2,3,0,2]
#prices = [1]
print(a.maxProfit(prices))

from typing import List

class Solution:
	def maxProfit(self, prices: List[int], fee: int) -> int:
		n = len(prices)
		buy = -prices[0]
		sell = 0
		for i in range(1, n):
			buy, sell = max(buy, sell - prices[i]), max(sell, buy + prices[i] - fee)	
		return sell


a = Solution()
prices = [1,3,2,8,4,9]; fee = 2
#prices = [1,3,7,5,10,3]; fee = 3
print(a.maxProfit(prices, fee))
			
				
				
			
				

from typing import List
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		buy = [float('-inf')] * n
		sell = [0] * n 
		
		buy[0] = -prices[0]
		for i in range(1, n):
			sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
			buy[i] = max(buy[i - 1], (sell[i - 2] if i > 1 else 0)  - prices[i])
		return sell[-1]	
		
a = Solution()
prices = [1,2,3,0,2]
prices = [1]
print(a.maxProfit(prices))

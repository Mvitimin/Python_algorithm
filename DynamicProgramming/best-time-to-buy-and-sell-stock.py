from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		cost = float('inf')
		profit = float('-inf')
		for i in range(len(prices)):
			cost = min(prices[i], cost)
			profit = max(prices[i] - cost, profit)
		return profit
		
a = Solution()
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(a.maxProfit(prices))

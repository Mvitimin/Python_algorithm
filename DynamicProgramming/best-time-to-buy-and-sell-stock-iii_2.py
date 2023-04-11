from typing import List
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		
		cost1 = cost2 = float('inf')
		profit1 = profit2 = float('-inf')
		for i in range(len(prices)):
			cost1 = min(cost1, prices[i])
			profit1 = max(profit1, prices[i] - cost1)
			cost2 = min(cost2, prices[i] - profit1)
			profit2 = max(profit2, prices[i] - cost2)
		return profit2

a = Solution()
prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [1]
print(a.maxProfit(prices))

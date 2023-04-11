from typing import List

class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		if k == 0:
			return 0	
		costs = [float('inf')] * k 
		profits = [0] * k
		for i in range(len(prices)):
			costs[0] = min(costs[0], prices[i])
			profits[0] = max(profits[0], prices[i] - costs[0])
			for j in range(1, k):
				costs[j] = min(costs[j], prices[i] - profits[j - 1])
				profits[j] = max(profits[j], prices[i] - costs[j])
			print(costs, profits)
		return profits[-1]

a = Solution()
k = 2; prices = [2,4,1]
k = 2; prices = [3,2,6,5,0,3]
#k = 2; prices = []
print(a.maxProfit(k, prices))

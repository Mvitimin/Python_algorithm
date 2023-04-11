from typing import List

class Solution:
	def minCost(self, costs: List[List[int]]) -> int:
		n = len(costs[0])
		
		for i in range(1, len(costs)):
			for j in range(n):
				v = float('inf')
				for k in range(n):
					if k != j:
						v = min(v, costs[i - 1][k])
				costs[i][j] += v		
		return min(costs[-1])

a = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
costs = [[7,6,2]]
print(a.minCost(costs))			


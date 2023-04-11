from typing import List

class Solution:
	def minimumCost(self, cost: List[int]) -> int:
		i = 0
		cost.sort(reverse=True)
		n = len(cost)
		ans = 0
		while i < n: 
			ans += cost[i]
			if i + 1 < n: ans += cost[i + 1]
			i += 3
		return ans

a = Solution()
cost = [5, 2, 1, 1]
print(a.minimumCost(cost))	
			

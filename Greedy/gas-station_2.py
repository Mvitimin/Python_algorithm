from typing import List

class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		if sum(gas) < sum(cost):
			return -1 
		g = ans = 0
		for i in range(len(gas)):
			g += gas[i] - cost[i]
			if g < 0:
				g = 0
				ans = i + 1
		return ans 
		
a = Solution()
gas = [1,2,3,4,5]; cost = [3,4,5,1,2]
print(a.canCompleteCircuit(gas, cost))		
			
			


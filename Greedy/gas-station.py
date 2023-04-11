from typing import List

class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		if sum(gas) - sum(cost) < 0:
			return -1 
		fuel = start = 0
		for i in range(len(gas)):
			if fuel + (gas[i] - cost[i]) < 0:
				start += 1
				fuel = 0
			else:
				fuel += (gas[i] - cost[i])
		return start
		

			
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

a = Solution()
print(a.canCompleteCircuit(gas, cost))

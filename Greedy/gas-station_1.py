from typing import List

class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		if sum(gas) < sum(cost):
			return -1		
		
		gas_sum, ans = 0, 0
		for i, g in enumerate(gas):
			gas_sum += (g - cost[i])
			if gas_sum < 0:
				ans = i + 1
				gas_sum = 0
				
		return ans 
			


a = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
#gas = [2,3,4]
#cost = [3,4,3]
gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(a.canCompleteCircuit(gas, cost))

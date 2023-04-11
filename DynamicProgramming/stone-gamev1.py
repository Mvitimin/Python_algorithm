from typing import List

class Solution:
	def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
		stones = [[i, aliceValues[i] + bobValues[i]] for i in range(len(aliceValues))]
		stones.sort(key=lambda x:x[1], reverse=True)
		
		alice = bob ]= 0
		for i in range(len(stones)):
			if i % 2 == 0:
				alice += aliceValues[stones[i][0]]
			else:
				bob += bobValues[stones[i][0]]
		
		if alice > bob:
			return 1
		elif alice < bob:
			return -1
		else:
			return 0

a = Solution()
aliceValues = [1,3]
bobValues = [2,1]
aliceValues = [1,2]
bobValues = [3,1]
aliceValues = [2,4,3]
bobValues = [1,6,7]
print(a.stoneGameVI(aliceValues, bobValues))
			


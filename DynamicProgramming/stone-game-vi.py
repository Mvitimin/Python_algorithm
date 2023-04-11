from typing import List

class Solution:
	def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
		
		n = len(aliceValues)
		array = []
		for i in range(n):
			array.append((i, aliceValues[i] + bobValues[i]))
		array.sort(key=lambda x:x[1], reverse=True)
		
		val = 0
		for i in range(n):
			if i % 2 == 0:
				val += aliceValues[array[i][0]]
			else:
				val -= bobValues[array[i][0]]
		
		if val < 0:
			return -1
		elif val > 0:
			return 1 
		else: return 0

aliceValues = [1,3]; bobValues = [2,1]
aliceValues = [1,2]; bobValues = [3,1]
#aliceValues = [2,4,3]; bobValues = [1,6,7]
a = Solution()
print(a.stoneGameVI(aliceValues, bobValues))
	

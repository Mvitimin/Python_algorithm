from typing import List

class Solution:
	def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
		boxTypes.sort(key=lambda x : x[1], reverse=True)
		ans = 0
		for i in range(len(boxTypes)):
			if truckSize > 0:
				box = boxTypes[i][0] if truckSize > boxTypes[i][0] else truckSize
				truckSize -= box
				ans += box * boxTypes[i][1]
			else:
				break
		return ans
			
a = Solution()
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(a.maximumUnits(boxTypes, truckSize))	


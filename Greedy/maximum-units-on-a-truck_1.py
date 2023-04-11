from typing import List

class Solution:
	def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
		n = len(boxTypes)
		
		boxTypes.sort(key=lambda x : -x[1])
		ans = 0
		for i in range(n):
			k = min(boxTypes[i][0], truckSize)
			ans += k * boxTypes[i][1]
			truckSize -= k
			if truckSize == 0:
				break
		return ans

a = Solution()
boxTypes = [[1,3],[2,2],[3,1]]; truckSize = 4
boxTypes = [[5,10],[2,5],[4,7],[3,9]]; truckSize = 10
print(a.maximumUnits(boxTypes, truckSize))
			
					

from typing import List

class Solution:
	def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:	
		boxes.sort(reverse=True)
		n = len(warehouse)
		m = len(boxes)
		
		dp = [0] * n 
		dp[0] = warehouse[0]
		for i in range(1, n):
			dp[i] = min(dp[i - 1], warehouse[i])
			
		for i in range(n - 1, -1, -1):
			if boxes and boxes[-1] <= dp[i]:
				boxes.pop()
		
		return m - len(boxes)		

a = Solution()
boxes = [4,3,4,1]; warehouse = [5,3,3,4,1]
#boxes = [1,2,2,3,4]; warehouse = [3,4,1,2]
#boxes = [1,2,3]; warehouse = [1,2,3,4]
print(a.maxBoxesInWarehouse(boxes, warehouse))

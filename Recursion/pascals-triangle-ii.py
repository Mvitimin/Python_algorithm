from typing import List

class Solution:
	def getRow(self, rowIndex: int) -> List[int]:	
		dp = [0] * (rowIndex + 1)
		dp[0] = 1
		
		for i in range(rowIndex + 1):
			k = 0
			for j in range(i + 1):
				k, dp[j] = dp[j], k + dp[j]
			dp[i] = 1	
		return dp		
			
a = Solution()
print(a.getRow(2))
		
		
			
			
		

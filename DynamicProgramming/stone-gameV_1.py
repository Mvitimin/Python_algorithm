from typing import List
from functools import lru_cache
class Solution:
	def stoneGameV(self, stoneValue: List[int]) -> int:
		
		n = len(stoneValue)
		dp = [[0] * (n + 1) for _ in range(n)]	
		
		for start in range(n - 2, -1, -1):
			for end in range(start + 2, n + 1):
				if left <= right:
					dp[start][end] = max(dp[start][end], left + dp[start][mid])
				if right <= left:
					dp[start][end] = max(dp[start][end], right + dp[mid][end])
				mid += 1
		print(dp)
		return dp[0][n]

a = Solution()
stoneValue = [6,2,3,4,5,5]
#stoneValue = [7,7,7,7,7,7,7]
#stoneValue = [4]
#stoneValue = [10,9,8,7,6,5,4,3,2,1]
#stoneValue = [68,75,25,50,34,29,77,1,2,69]
print(a.stoneGameV(stoneValue))
			
																								

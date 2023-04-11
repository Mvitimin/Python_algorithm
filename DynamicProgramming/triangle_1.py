from typing import List
from functools import lru_cache

class Solution:
	def minimumTotal(self, triangle: List[List[int]]) -> int:
		n = len(triangle)
		m = len(triangle[-1])
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(n - 1, -1, -1):
			for j in range(len(triangle[i])):
				dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
		return dp[0][0]
			

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
a = Solution()
print(a.minimumTotal(triangle))

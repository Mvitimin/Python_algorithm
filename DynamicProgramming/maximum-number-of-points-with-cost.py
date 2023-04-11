from typing import List

class Solution:
	def maxPoints(self, points: List[List[int]]) -> int:
		m, n = len(points), len(points[0])
		dp = [[0] * n for _ in range(m)]
		dp[0] = points[0][:]
		
		for i in range(1, m):
			tmp = 0
			for j in range(n):
				tmp = max(tmp, dp[i - 1][j])
				dp[i][j] = max(dp[i][j], tmp + points[i][j])
				tmp -= 1
			tmp = 0
			for j in range(n - 1, -1, -1):
				tmp = max(tmp, dp[i - 1][j])
				dp[i][j] = max(dp[i][j], tmp + points[i][j])
				tmp -= 1
		return max(dp[-1])		
		
a = Solution()
points = [[1,2,3],[1,5,1],[3,1,1]]
points = [[1,5],[2,3],[4,2]]
print(a.maxPoints(points))

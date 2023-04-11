from typing import List

class Solution:
	def stoneGameVII(self, stones: List[int]) -> int:
		n = len(stones)
		dp = [[0] * (n + 1) for _ in range(n + 1)]
		
		for i in range(n - 2, -1, -1):
			for j in range(i + 1, n):
				dp[i][j] = max(min(stones[i + 1] + dp[i + 2][j], 
				stones[j] + dp[i + 1][j - 1]),
				min(stones[i] + dp[i + 1][j - 1], stones[j - 1] + dp[i][j - 2]))
		return dp[0][n - 1]
		
		
a = Solution()
stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]
print(a.stoneGameVII(stones))

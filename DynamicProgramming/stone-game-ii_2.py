from typing import List

class Solution:
	def stoneGameII(self, piles: List[int]) -> int:
		n = len(piles)
		dp = [[0] * (n + 1) for i in range(n)]
		for j in range(n - 2, -1, -1):
			piles[j] += piles[j + 1]
		
		for i in range(n - 1, -1, -1):
			for m in range(n, 0, -1):
				for j in range(1, 2 * m + 1):
					val = piles[i] - dp[i + j][max(m, j)] if i + j < n else piles[i]
					dp[i][m] = max(dp[i][m], val) 
		return dp[0][1]
						
		
a = Solution()
piles = [2,7,9,4,4]
#piles = [1,2,3,4,5,100]
print(a.stoneGameII(piles))


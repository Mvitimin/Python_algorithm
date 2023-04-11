from typing import List

class Solution:
	def stoneGameII(self, piles: List[int]) -> int:
		n = len(piles)
		pre_sum = [0] * (n + 1)
		for i in range(n - 1, -1, -1):
			pre_sum[i] = piles[i] + pre_sum[i + 1]
		
		dp = [[0] * (n + 1) for _ in range(n + 1)]
		for i in range(n - 1, -1, -1):
			for m in range(1, n + 1):
				dp[i][m] = float('-inf')
				for x in range(1, min(2 * m + 1, n + 1)):
					if i + x <= n:
						dp[i][m] = max(dp[i][m], pre_sum[i] - dp[i + x][max(x, m)]) 
		print(dp)
		return dp[0][1]
				
				
a = Solution()
#piles = [1]
piles = [2,7,9,4,4]
#piles = [1,2,3,4,5,100]
print(a.stoneGameII(piles))

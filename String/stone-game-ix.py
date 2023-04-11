from typing import List

class Solution:
	def stoneGameIX(self, stones: List[int]) -> bool:
		dp = [0] * 3
		for s in stones:
			dp[s % 3] += 1
		if dp[0] % 2 == 0:
			return dp[1] * dp[2] > 0
		else:
			return abs(dp[2] - dp[1]) > 2
				

a = Solution()
stones = [5,1,2,4,3]
#stones = [2, 3, 2]
#stones = [2,1]
print(a.stoneGameIX(stones))

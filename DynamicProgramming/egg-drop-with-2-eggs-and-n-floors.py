
class Solution:
	def twoEggDrop(self, n: int) -> int:
		dp = [float('inf')] * (n + 1)
		dp[0] = dp[1] = 1
		
		for i in range(2, n + 1):
			for j in range(1, i):
				dp[i] = min(dp[i], 1 + max(j - 1, dp[i - j])) 
		return dp[-1]	
		
a = Solution()
n = 100
print(a.twoEggDrop(n))

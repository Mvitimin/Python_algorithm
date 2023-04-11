class Solution:
	def minSteps(self, n: int) -> int:
		if n <= 1:
			return 0
		dp = [i for i in range(n + 1)]
		for i in range(2, n + 1):
			for j in range(2, i):
				if i % j == 0:
					dp[i] = min(dp[i], dp[j] + i // j)					
		return dp[n]
		
a = Solution()
print(a.minSteps(4))	
						

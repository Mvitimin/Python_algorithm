class Solution:
	def divisorGame(self, n: int) -> bool:		
		if n <= 1:
			return False
		dp = [False] * (n + 1)
		dp[2] = True
		for i in range(3, n + 1):
			for j in range(1, i):
				if i % j == 0 and not dp[i - j]:
					dp[i] = True
					break
		return dp[n]
			
			
a = Solution()
n = 2
n = 3
n = 8
print(a.divisorGame(n))


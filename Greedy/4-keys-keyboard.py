class Solution:
	def maxA(self, n: int) -> int:
		if n <= 3:
			return n
		dp = [0] * (n + 1)
		dp[1], dp[2], dp[3] = 1, 2, 3
		for i in range(4, n + 1):
			dp[i] = max([dp[i - 1] + 1] + [dp[i - j] * (j - 1) for j in range(3, i)])
		return dp[n]
		
a = Solution()
#n = 10
n = 8
n = 11
n = 9
#n = 6
print(a.maxA(n))	
			
	

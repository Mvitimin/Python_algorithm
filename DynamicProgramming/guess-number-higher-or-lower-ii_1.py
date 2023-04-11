
class Solution:
	def getMoneyAmount(self, n: int) -> int:
		dp = [[0] * (n + 2) for _ in range(n + 2)]
		for i in range(n, 0, -1):
			for j in range(i + 1, n + 1):
				val = float('inf')
				for k in range(i, j + 1):
					val = min(val, k + max(dp[k + 1][j], dp[i][k - 1]))
				dp[i][j] = val 	
		
		for i in range(n + 1):
			for j in range(n + 1):
				print('{:2d}'.format(dp[i][j]), end=' ')
			print()
			
		return dp[1][10] 
		
a = Solution()
n = 10
print(a.getMoneyAmount(n))

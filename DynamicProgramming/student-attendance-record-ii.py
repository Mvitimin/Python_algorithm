class Solution:                                 
	def checkRecord(self, n: int) -> int:   
		
		dp = [0] * (max(n + 1, 5))
		dp[0] = 1
		dp[1] = 2
		dp[2] = 4
		dp[3] = 7 # LLL(x)
		M = 10 ** 9 + 7
		for i in range(4, n + 1):
			dp[i] = (dp[i - 1] * 2 - dp[i - 4]) % M
		
		ans = 0
		for i in range(1, n + 1):
			ans += (dp[i - 1] * dp[n - i]) % M
		return (ans + dp[n]) % M

'''
solve(6, '')
print(ans)
print("real", len(ans))
'''

a = Solution()
n = 2
n = 10101
#n = 99991
#n = 4
#n = 2
print(a.checkRecord(n))


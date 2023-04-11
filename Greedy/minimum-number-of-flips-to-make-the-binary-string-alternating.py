class Solution:
	def minFlips(self, s: str) -> int:
		n = len(s)
		if n <= 1:
			return 0
		dp = [[0] * 2 for _ in range(n)]			
		k = int(s[0])
		dp[0][k ^ 1] = 1
		for i in range(1, n):
			k = int(s[i])
			dp[i][k ^ 1] = dp[i - 1][k] + 1
			dp[i][k] = dp[i - 1][k ^ 1]
		
		ans = min(dp[-1])
		
		for i in range(n - 1):
			#print(i, 0 ^ (n - 1) % 2)
			ans = min(ans, dp[-1][0] - dp[i][0 ^ (n - i - 1) % 2] + dp[i][1 ^ i % 2])
			ans = min(ans, dp[-1][1] - dp[i][1 ^ (n - i - 1) % 2] + dp[i][0 ^ i % 2])
				
		return ans			
		
		
				
		
		
a = Solution()
s = "111000"
s = "01001001101"
#s = "010"
#s = "1110"
print(a.minFlips(s))				
	
		
		
		
		
			
		
			

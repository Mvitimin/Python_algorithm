
class Solution:
	def countDigitOne(self, n: int) -> int:		
		if n <= 1: return n
		if n <= 9: return 1
		t = str(n)[::-1]
		m = len(t)
		num = int(t[0])
				
		dp = [[0] * (m + 1) for _ in range(m)]	
		dp2 = [[0] * (m + 1) for _ in range(m)]
		dp[0][0], dp[0][1] = 9, 1 
		if num > 1:
			dp2[0][0], dp2[0][1] = num, 1
		else: 
			dp2[0][0], dp2[0][1] = 1, int(num == 1)
			
		for i in range(1, m):
			digit = int(t[i])
			num += (digit * (10 ** i))
			s = 0
			for	j in range(1, i + 2):
				dp[i][j] = 9 * dp[i - 1][j] + dp[i - 1][j - 1]
				if digit > 1:
					dp2[i][j]	= dp[i - 1][j] * (digit - 1) + dp[i - 1][j - 1] + dp2[i - 1][j] 
				elif digit == 1:
					dp2[i][j] = dp[i - 1][j] + dp2[i - 1][j - 1]
				else:
					dp2[i][j] = dp2[i - 1][j]
				s += dp2[i][j]	
				
			dp[i][0], dp2[i][0] = 9 ** (i + 1), num - s + 1 
		
		ans = 0
		for i in range(1, m + 1):
			ans += dp2[-1][i] * i 
		return ans
		
		
a = Solution()
n = 100
n = 101
print(a.countDigitOne(n))				
				
				
			
				
				
				
				
				
				
		

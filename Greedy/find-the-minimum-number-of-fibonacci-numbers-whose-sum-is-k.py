import bisect

class Solution:
	def findMinFibonacciNumbers(self, k: int) -> int:
		MAX_VAL = 45
		
		dp = [0] * (MAX_VAL + 1)
		dp[0] = dp[1] = dp[2] = 1
		
		# 45 
		for i in range(3, MAX_VAL + 1):
			dp[i] = dp[i - 1] + dp[i - 2]
		
		cnt = 0
		while k:		
			for i in range(MAX_VAL, 1, -1):
				if k >= dp[i]:
					cnt += 1
					k -= dp[i]
					break
		return cnt 
			
	
			
a = Solution()
k = 7
k = 10
k = 19
print(a.findMinFibonacciNumbers(k))

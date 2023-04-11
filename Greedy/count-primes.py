class Solution:
	def countPrimes(self, n: int) -> int:
		if n <= 2:
			return 0
		
		dp = [False, False] + [True] * (n - 2)
		
		
		for i in range(2, int(n ** 0.5) + 1):
			if dp[i]:
				for j in range(i * 2, n, i):
					dp[j] = False
	
		return sum(dp)		
			
			
				
a = Solution()
n = 10
print(a.countPrimes(n))

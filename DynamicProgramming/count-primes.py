
import math
class Solution:
	def countPrimes(self, n: int) -> int:
		if n <= 2:
			return 0
		
		dp = [False, False] + [True] * (n - 2)
		
		for p in range(2, int(n ** 0.5) + 1):
			if dp[p]:
				for multiple in range(p * p, n, p):
					dp[multiple] = False
		return sum(dp)							
			
		
		
			
														
																																				
#1, 4, 6, 8, 9, 10																	
a = Solution()
print(a.countPrimes(10))					
		

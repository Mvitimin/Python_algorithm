from typing import List

class Solution:
	def largestMultipleOfThree(self, digits: List[int]) -> str:
		n = len(digits)
		dp = [float('-inf')] * 3
		digits.sort(reverse=True)
		dp[digits[0] % 3] = digits[0]
		for i in range(1, n):
			prev = dp[:]
			dp = [float('-inf')] * 3
			d = digits[i] 
			dp[d % 3] = digits[i]
			for j in range(3):
				k = (d + j) % 3
				if prev[j] != float('-inf'):
					dp[k] = max(d + prev[j] * 10, prev[k])
				else: dp[k] = max(prev[k], dp[k])
		return str(dp[0]) if dp[0] != float('-inf') else '' 
					
			 
	
a = Solution()
digits = [8, 1, 9]
#digits = [8,6,7,1,0]
#digits = [1]
#digits = [0,0,0,0,0,0]
#digits = [1]
#digits = [1,1,1,2]
digits = [5, 8]
print(a.largestMultipleOfThree(digits))

print(774 % 3)
			
			
			
			


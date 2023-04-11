from typing import List
import collections
class Solution:
	def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(len(strs)):
			counter = collections.Counter(strs[i])
			for j in range(m, counter['0'] - 1 , -1):
				for k in range(n, counter['1'] - 1, -1):
					dp[j][k] = max(dp[j][k], dp[j - counter['0']][k - counter['1']] + 1)
		return dp[m][n]
		
		

a = Solution()
strs = ["10","0001","111001","1","0"]; m = 5; n = 3
#strs = ["10","0","1"]; m = 1; n = 1
#strs = ["10","0001","111001","1","0"]; m = 4; n= 3
strs = ["10","0001","111001","1","0"]; m = 50; n = 50
result = a.findMaxForm(strs, m, n)
print(result)

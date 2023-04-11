from typing import List

class Solution:
	def findLongestChain(self, pairs: List[List[int]]) -> int:
		n = len(pairs)
		pairs.sort()
		dp = [1] * n 
		for i in range(n):
			for j in range(n - 1):
				if pairs[j][1] < pairs[i][0]: 
					dp[i] = max(dp[j] + 1, dp[i])	
		return max(dp)	
a = Solution()
pairs = [[1,2],[2,3],[3,4]]
#pairs = [[1,2],[7,8],[4,5]]
print(a.findLongestChain(pairs))

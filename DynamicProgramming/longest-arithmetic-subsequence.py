from typing import List
import copy
import collections

class Solution:
	def longestArithSeqLength(self, A: List[int]) -> int:
		dp = []
		for i in range(len(A)):
			dp.append(collections.defaultdict(lambda :1))
		ans = 0
		for i in range(len(A)):
			for j in range(0, i):
				dp[i][A[i] - A[j]] = dp[j][A[i] - A[j]] + 1
				ans = max(ans, dp[i][A[i] - A[j]])
			#print(i, dp[i])
		return ans




#A = [9,4,7,2,10]
#A = [3, 6, 9, 12]
A = [20, 1, 15, 3, 10, 5, 8]
a = Solution()
print(a.longestArithSeqLength(A))

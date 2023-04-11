#https://leetcode.com/problems/reorganize-string/solution/

import collections

class Solution:
	def reorganizeString(self, S: str) -> str:
		
		N = len(S)
		A = []
		for c, x in sorted((S.count(x), x) for x in set(S)):
			if c > (N + 1)// 2 : return ""
			A.extend(c * x)
		ans = [i for i in range(N)]
		ans[::2], ans[1::2] = A[N//2:], A[:N//2]
		return "".join(ans)
		
#S = "aaaaacccccbbbbb"
#S = "a"
S = "vvvvlo"
#S = "aaaabbbbccc"
a = Solution()
print(a.reorganizeString(S))
		
		

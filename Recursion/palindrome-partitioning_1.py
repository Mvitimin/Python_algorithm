from typing import List

class Solution:
	def partition(self, s: str) -> List[List[str]]:
		n = len(s)
		
		if n <= 0:
			return [[s]]
		
		dp = [[False] * n for _ in range(n)]
		
		for i in range(n):
			dp[i][i] = True
			if i + 1 < n:
				dp[i + 1][i] = True
		
		for l in range(2, n + 1):
			for i in range(n):
				j = (l + i - 1)
				if i < j < n:
					dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
		
		ans = []
		tmp = []				
		def solve(i):
			if i >= n:
				ans.append(tmp[:])
				
			for j in range(i, n):
				if dp[i][j]:
					tmp.append(s[i:j + 1])
					solve(j + 1)
					tmp.pop()
					
		solve(0)
		return ans
		
	
a = Solution()
s = "bca"
s = "aab"
print(a.partition(s))

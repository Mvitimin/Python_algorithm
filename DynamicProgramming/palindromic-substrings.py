from functools import lru_cache

class Solution:
	def countSubstrings(self, s: str) -> int:
		n = len(s)
		if n <= 1:
			return n
		
		@lru_cache(None)
		def dp(i, j):
			if i >= j: return 1
			return dp(i + 1, j - 1) if s[i] == s[j] else 0
		
		ans = 0
		for i in range(n):
			for j in range(i, n):
				ans += dp(i, j)	
		return ans	
a = Solution()
s = "aaaaa"
print(a.countSubstrings(s))
				
				
				

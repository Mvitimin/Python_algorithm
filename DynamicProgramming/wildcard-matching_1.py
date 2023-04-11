from functools import lru_cache
class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		n, m = len(s), len(p)
		
		@lru_cache(None)
		def helper(s_index, p_index):
			if (p_index >= m):
				return s_index >= n
					
			if s_index <= n - 1 and p[p_index] in ['?', s[s_index], '*']:
				if helper(s_index + 1, p_index + 1):
					return True
			if p[p_index] == '*':
				if helper(s_index, p_index + 1):
					return True
				if s_index <= n - 1 and helper(s_index + 1, p_index):
					return True
			return False
		return helper(0, 0)

a = Solution()
s = "cb"; p = "?a"
#s = "adceb"; p = "*a*b"
#s = "acdcb"; p = "a*c?b"
#s = ""; p = "******"
#s = "abcabczzzde"; p = "*abc???de*"
print(a.isMatch(s, p))

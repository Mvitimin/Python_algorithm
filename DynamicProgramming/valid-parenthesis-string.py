from functools import lru_cache

class Solution:
	def checkValidString(self, s: str) -> bool:
		n = len(s)
		
		@lru_cache(None)
		def solve(i, left):
			if i == n:
				return left == 0
			if s[i] in '(': 
				if solve(i + 1, left + 1): return True
			elif s[i] in ')':
				if left and solve(i + 1, left - 1): return True
			else: 
				if solve(i + 1, left + 1) or (left and solve(i + 1, left - 1)) or solve(i + 1, left): return True 
			return False
		return solve(0, 0)

a = Solution()
s = "()*)*)"
print(a.checkValidString(s))


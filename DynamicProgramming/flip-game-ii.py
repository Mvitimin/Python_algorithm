from functools import lru_cache

class Solution:
	def canWin(self, currentState: str) -> bool:
		k = 1 
		p = 60
		while p > 3:
			k *= (p - 2)
			p -= 2
		print(k)
		
		
		@lru_cache(None)
		def dp(s):
			for i in range(len(s)):
				if s[i:i + 2] == '++':
					if not dp(s[:i] + '--' + s[i + 2:]):
						return True
			return False
		return dp(currentState)
		
		
a = Solution()
currentState = "++++--++++"
currentState = "++++"
#currentState = "+---"
#currentState = "++"
print(a.canWin(currentState))

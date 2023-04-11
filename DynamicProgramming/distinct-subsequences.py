import collections
from functools import lru_cache

class Solution:
	def numDistinct(self, s: str, t: str) -> int:
		count_s = collections.Counter(s)
		count_t = collections.Counter(t)
		n, m = len(s), len(t)
		@lru_cache(None)
		def dp(i, j):
			if i == n or j == m:
				if i <= n and j == m:
					return 1
				else:
					return 0 		
			cnt = 0
			count_s[s[i]] -= 1
			if s[i] == t[j]:
				count_t[t[j]] -= 1
				cnt += dp(i + 1, j + 1)
				count_t[t[j]] += 1
			
			if count_s[t[j]] >= count_t[t[j]]:
				cnt += dp(i + 1, j)
			count_s[s[i]] += 1
			return cnt		
		return dp(0, 0)

a = Solution()
s = "rabbbit"; t = "rabbit"
#s = "babgbag"; t = "bag"
print(a.numDistinct(s, t))

				
				
	

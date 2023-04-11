from functools import lru_cache

class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		n, m, l = len(s1), len(s2), len(s3)
		
		@lru_cache(None)
		def dp(i, j, k):
			if i == n and j == m and k == l:
				return True
						
			if k < l:
				if i < n and s3[k] == s1[i]:
					if dp(i + 1, j, k + 1):
						return True
				if j < m and s3[k] == s2[j]:
					if dp(i, j + 1, k + 1):
						return True
			return False
		
		if n + m == l:
			return dp(0, 0, 0)
		else:
			return False	
			
a = Solution()
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
s1 = ""; s2 = ""; s3 = ""
print(a.isInterleave(s1, s2, s3))

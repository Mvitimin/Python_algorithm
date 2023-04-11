from functools import lru_cache

class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		n, m, l = len(s1), len(s2), len(s3)
		if n + m != l: return False
		dp = [False] * (m + 1)
		prev = [False] * (m + 1)
		for i in range(n + 1):
			for j in range(m + 1):
				if i == 0 and j == 0:
					dp[0] = True
				else:
					dp[j] = (i > 0 and prev[j] and s1[i - 1] == s3[i + j - 1])\
					or (j > 0 and dp[j - 1] and s2[j - 1] == s3[i + j - 1])
			prev, dp = dp, [False] * (m + 1)		
		return prev[-1]					
				
					
					
								
					
			
a = Solution()
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
s1 = ""; s2 = ""; s3 = ""
print(a.isInterleave(s1, s2, s3))

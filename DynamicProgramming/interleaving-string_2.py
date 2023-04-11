
class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
		m, n, l = len(s1), len(s2), len(s3)
		if (m + n) != l:
			return False
		if s1 + s2 == s3 or s2 + s1 == s3: return True
		dp = [[False] * (n + 1) for _ in range(m + 1)]
		dp[0][0] = True			
		for i in range(0, m + 1):
			if dp[i - 1][0] and s3[i - 1] == s1[i - 1]:
				dp[i][0] = True
			for j in range(1, n + 1):
				if i == 0:
					if dp[0][j - 1] and s3[j - 1] == s2[j - 1]: 
						dp[0][j] = True
					else: break			
				idx = i + j - 1
				if (dp[i][j - 1] and s3[idx] == s2[j - 1]) or (dp[i - 1][j] and s3[idx] == s1[i - 1]):
					dp[i][j] = True
		return dp[-1][-1]
			
a = Solution()
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"
s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
s1 = ""; s2 = ""; s3 = ""
#s1 = "a"; s2 = "b"; s3 = "a"
#s1 = "a"; s2 = ""; s3 = "a"
#s1 = "aaaa"; s2 = "aa"; s3 = "aaa"
print(a.isInterleave(s1, s2, s3))

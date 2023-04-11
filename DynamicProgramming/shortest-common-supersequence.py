class Solution:
	def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
		n, m = len(str1), len(str2)
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if str1[i - 1] == str2[j - 1]:
					dp[i][j] = dp[i - 1][j - 1] + 1
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
		print(dp)
		i, j = n, m 
		res = ''
		while i > 0 or j > 0:
			if i > 0 and dp[i][j] == dp[i - 1][j]:
				i -= 1
				res = str1[i] + res
				print(i, j, res)
			elif j > 0 and dp[i][j] == dp[i][j - 1]:
				j -= 1
				res = str2[j] + res
			else:
				i -= 1
				j -= 1
				res = str1[i] + res
										
		return res					
						
a = Solution()
str1 = "abac"; str2 = "cab"			
#str1 = "aaaaaaaa"; str2 = "aaaaaaaa"		
#str1 = "bbbaaaba"; str2 = "bbababbb"
print(len("bbababbaaba"), len("bbabaaababb"))
ans = a.shortestCommonSupersequence(str1, str2)
print(ans)	
				
				


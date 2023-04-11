from typing import List

class Solution:
	def differByOne(self, dict: List[str]) -> bool:
		
		m, n = len(dict), len(dict[0])
		dp = [0] * m
		MOD = 10 ** 12
		
		for j in range(n):
			for i in range(m):
				dp[i] = (dp[i] * 26 + ord(dict[i][j]) - ord('a')) % MOD
		
		val = 1
		for j in range(n - 1, -1, -1):
			visited = set()
			for i in range(m):
				k = (dp[i] - (ord(dict[i][j]) - ord('a')) * val) % MOD
				if k in visited:
					return True
				visited.add(k)	
			val = (val * 26) % MOD
		return False
		
a = Solution()
dict = ["abcd","acbd", "aacd"]
dict = ["ab","cd","yz"]
dict = ["abcd","cccc","abyd","abab"]
dict = ["abcde","addde","abbbe","xbcde","feabc"]
dict = ["abcde","abaaa","aaade"]
print(a.differByOne(dict))

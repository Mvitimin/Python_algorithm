from typing import List

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		words = set(wordDict)
		dp, n = {}, len(s)
		def solve(start):
			if start >= len(s):
				return True
			if start in dp:
				return dp[start]
			for end in range(start + 1, n + 1):
				if s[start:end] in words and solve(end):
						dp[start] = True
						return dp[start]
			dp[start] = False
			return dp[start]
		return solve(0)
					
a = Solution() 
s = "leetcode"; wordDict = ["leet","code"]
s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]
s = "applepenapple"; wordDict = ["apple","pen"]
print(a.wordBreak(s, wordDict))

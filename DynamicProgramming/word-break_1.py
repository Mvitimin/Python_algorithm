from typing import List

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		words, n = set(wordDict), len(s)
		dp = [False] * (n + 1)
		dp[n] = True
		for start in range(n - 1, -1, -1):
			for end in range(start + 1, n + 1):
				if s[start:end] in words and dp[end]:
					dp[start] = True
					break
		return dp[0]
		
					
a = Solution() 
s = "leetcode"; wordDict = ["leet","code"]
s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]
#s = "applepenapple"; wordDict = ["apple","pen"]
print(a.wordBreak(s, wordDict))

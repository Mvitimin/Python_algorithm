from typing import List
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		
		n = len(wordDict)
		dp = {}
		for i in range(len(s) + 1):
			dp[s[:i]] = False
		dp[''] = True
		
		for t in dp:
			if not dp[t]: continue
			for i in range(n):
				tmp = t + wordDict[i]
				if tmp in dp: dp[tmp] = True
		return dp[s]

						
a = Solution()
s = "leetcode"; wordDict = ["leet","code"]

#s = "applepenapple"; wordDict = ["apple","pen"]

#s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]
print(a.wordBreak(s, wordDict))

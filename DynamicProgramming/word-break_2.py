from typing import List
from functools import lru_cache

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		
		n = len(wordDict)
		
		def isPrefix(word):
			if len(word) > len(s): return False
			for i, c in enumerate(word):
				if s[i] != c: return False
			return True
			
		@lru_cache(None)			
		def dp(t):
			if len(t) == len(s): return True
			for i in range(n):
				tmp = t + wordDict[i]
				if isPrefix(tmp) and dp(tmp): return True 
			return False
				
		return dp('')

						
a = Solution()
s = "leetcode"; wordDict = ["leet","code"]

s = "applepenapple"; wordDict = ["apple","pen"]

s = "catsandog"; wordDict = ["cats","dog","sand","and","cat"]
print(a.wordBreak(s, wordDict))

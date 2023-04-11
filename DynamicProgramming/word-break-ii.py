from typing import List
import collections
import copy

class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
		n = len(s)
		dp = collections.defaultdict(list)
		wordSet = set(wordDict)
		dp[0].append('')
		
		for i in range(n):
			dp2 = copy.copy(dp)
			for j in range(i + 1, n + 1):
				k = s[i:j]
				if k in wordSet:
					for text in dp[i]:
						dp2[j].append('{} {}'.format(text, k).lstrip())
			dp = dp2
		return dp[n]	
	


a = Solution()
#s = "catsanddog"; wordDict = ["cat","cats","and","sand","dog"]
s = "pineapplepenapple"; wordDict = ["apple","pen","applepen","pine","pineapple"]
print(a.wordBreak(s, wordDict))
#print(' hihi'.lstrip())	
		


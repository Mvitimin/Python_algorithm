#https://leetcode.com/problems/longest-string-chain/
import collections
from typing import List
class Solution:
	def longestStrChain(self, words: List[str]) -> int:
		if not words:
			return 0
		dp = collections.defaultdict(set)
		words.sort(key=len)
		for char in words[0]:
			dp[len(words[0])].add(char)
		max_len = len(words[0])	
		for i in range(1, len(words)):
			if not dp[len(words[i]) - 1]:
				continue
			cnt = 0
			
			for char in words[i]:
				if char not in dp[len(words[i]) - 1]:
					cnt += 1
			if cnt <= 1:
				max_len = len(words[i])
				for char in words[i]:
					dp[len(words[i])].add(char)
		return max_len - len(words[0]) + 1


#words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
words = ["a", "b", "ba", "xca", "bda", "bdca"]
a = Solution()
print(a.longestStrChain(words))

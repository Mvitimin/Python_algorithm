#https://leetcode.com/problems/longest-string-chain/
from typing import List
class Solution:
	def longestStrChain(self, words: List[str]) -> int:
		words.sort(key=len)
		dp = {}
		ans = 0
		for word in words:			
			cur = 1
			for i in range(len(word)):
				txt = word[:i] + word[i + 1:]
				if txt in dp: 
					cur = max(cur, dp[txt] + 1)
			dp[word] = cur
			ans = max(ans, cur)
		return ans


#words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
#words = ["a", "b", "ba", "xca", "bda", "bdca"]
#words = ['a', 'b', 'ab', 'bc']
words = ["a","ab","ac","bd","abc","abd","abdd"]
a = Solution()
print(a.longestStrChain(words))

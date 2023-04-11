from typing import List
import collections
class Solution:
	def longestPalindrome(self, words: List[str]) -> int:
		
		counter = collections.Counter(words)
		ans = 0
		flag = 0
		for word in words:
			if counter[word] <= 0:
				continue	
			counter[word] -= 1
			match = word[::-1]
			if counter[match] > 0:
				counter[match] -= 1
				ans += 4
			elif not flag and word == match:
				flag = 2
		return ans + flag	
				


a = Solution()
words = ["lc","cl","gg"]
words = ["ab","ty","yt","lc","cl","ab"]
words = ["cc","ll","xx"]
print(a.longestPalindrome(words))				
				
				
			

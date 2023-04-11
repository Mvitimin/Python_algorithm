import collections

class Solution:
	def longestPalindrome(self, s: str) -> int:
		counter = collections.Counter(s)
		
		ans = 0
		odd = False
		for c in counter:
			if counter[c] % 2 == 1:
				odd = True
			ans += (counter[c] // 2) * 2
		return ans + int(odd)
		
		

a = Solution()
s = "abccccdd"
s = "a"
print(a.longestPalindrome(s))	

import collections

class Solution:
	def longestPalindrome(self, s: str) -> int:
		counter = collections.Counter(s)
		n = len(counter)
		odd = 0
		ans = 0
		for c in counter:
			if counter[c] % 2 == 0:
				ans += counter[c]
			else:
				ans += max(0, counter[c] - 1)
				odd = 1
		return ans + odd	
		
			
a = Solution()
s = "abccccdd"
s = "a"
print(a.longestPalindrome(s))				

import collections

class Solution:
	def longestPalindrome(self, s: str) -> int:
		counter = collections.Counter(s)
		ans = odd = 0
		for c in counter:
			if counter[c] % 2 == 1:
				odd += 1
				counter[c] -= 1
			ans += counter[c]
		return ans + min(1, odd)		

a = Solution()
s = "abccccdd"
s = "a"
s = "bb"
print(a.longestPalindrome(s))

from collections import Counter
class Solution:
	def findTheDifference(self, s: str, t: str) -> str:
		counter = Counter(s)
		for c in t:
			counter[c] -= 1
			if counter[c] < 0:
				return c

a = Solution()
s = "abcd"; t = "abcde"
s = "a"; t = "aa"
s = "ae"; t = "aea"
print(a.findTheDifference(s, t))
print(ord('a'))

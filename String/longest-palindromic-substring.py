class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		if s == s[::-1]:
			return s
		
		def check(l, r):
			ans = 0
			while 0 <= l and r < n and s[l] == s[r]:
				ans = r - l + 1
				l -= 1
				r += 1
			return [l + 1, r - 1]
		
		ans = [0, 0]
		for i in range(n):
			ans = max(ans, check(i, i + 1), check(i, i), key=lambda x : x[1] - x[0] + 1)
		return s[ans[0]:ans[1] + 1]

a = Solution()
s = "babad"
#s = "cbbd"
print(a.longestPalindrome(s))
			

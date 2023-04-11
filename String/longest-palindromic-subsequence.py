class Solution:
	def longestPalindrome(self, s: str) -> str:
		n = len(s)
		
		def palindrome(l, r):
			while l >= 0 and r < n and s[l] == s[r]:
				l -= 1
				r += 1
			return (l + 1, r)			
		
		ans = (0, 1)
		for i in range(n):
			ans = max(ans, palindrome(i, i + 1), palindrome(i - 1, i + 1), key=lambda x: x[1] - x[0] - 1)	
		return s[ans[0]:ans[1]]
		
a = Solution()
s = "babad"
#s = "cbbd"
print(a.longestPalindrome(s))

class Solution:
	def longestPalindrome(self, s: str) -> str:
		
		n = len(s)
		if s[:] == s[::-1]:
			return s
		
		def palindrome(left, right):
			if s[left] != s[right]:
				return (left + 1, right - 1)
			
			while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
				left -= 1
				right += 1
				 						
			return (left, right)
		
		ans = (0, 0)
		
		for i in range(1, n):
			
			ans = max(ans, palindrome(i - 1, i), palindrome(i, i), key=lambda x:x[1] - x[0] + 1)	
			
		return s[ans[0]:ans[1] + 1]	
			
a = Solution()
s = "babad"
#s = "ac"
s = "cbbd"
print(a.longestPalindrome(s))

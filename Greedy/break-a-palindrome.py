class Solution:
	def breakPalindrome(self, palindrome: str) -> str:
		n = len(palindrome)
		i, j = 0, n - 1
		if n <= 1: return ''
		while i < j:
			if palindrome[i] > 'a':
				return palindrome[:i] + 'a' + palindrome[i + 1:]
			i += 1
			j -= 1			
		return palindrome[:n - 1] + 'b'		
				
a = Solution()				
palindrome = "abccba"
palindrome = "aaccaa"
palindrome = "aacaa"
print(a.breakPalindrome(palindrome))		

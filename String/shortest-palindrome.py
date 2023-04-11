class Solution:
	def shortestPalindrome(self, s: str) -> str:
		n = len(s)
				
		for i in range(n, -1, -1):
			prefix, postfix = s[:i], s[i:]
			if prefix == prefix[::-1]:
				return postfix[::-1] + prefix + postfix	
			
a = Solution()
s = "aacecaaa"
s = "abcd"
#s = "abkcba"
s = "abbacd"
print(a.shortestPalindrome(s))
				
				
				 		
		

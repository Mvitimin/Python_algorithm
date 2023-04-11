class Solution:
	def shortestPalindrome(self, s: str) -> str:
		n = len(s)
	
		for k in range(n - 1, -1, -1):
			i, j = 0, k
			while i <= j:
				if s[i] != s[j]:
					break
				i += 1
				j -= 1
			else:
				return s[n - 1:k:-1] + s
				
				
				
		return s[n - 1:0:-1] + s		
				
		
		
						
				
		
	
a = Solution()
#s = "aacecaaa"
#s = "abcd"

#s = "bkkbatpk"
s = "abb"
print(a.shortestPalindrome(s))
			

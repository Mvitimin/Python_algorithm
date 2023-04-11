from typing import List

class Solution:
	def findRepeatedDnaSequences(self, s: str) -> List[str]:
		n = len(s)
		def palindrome(l, r):
			while l >= 0 and r < n and s[l] == s[r]:
				l -= 1
				r += 1
			return s[l + 1:r]			
		
		ans = ''
		for i in range(n):
			ans = max(ans, palindrome(i, i + 1), palindrome(i - 1, i + 1), key=lambda x: len(x))	
		return 
			
		

a = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#print(a.findRepeatedDnaSequences(s))	
#print(4 ** 10)		
		


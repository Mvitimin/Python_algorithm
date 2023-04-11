from typing import List

class Solution:
	def largeGroupPositions(self, s: str) -> List[List[int]]:
		s = s + '#'
		prev = s[0]
		start = end = 0
		ans = []
		for i in range(1, len(s)):
			if s[i] != prev: 
				if i - start >= 3:
					ans.append([start, i - 1])
				start = i; prev = s[i]
		return ans 
		
		
a = Solution()
s = "abcdddeeeeaabbbcd"
s = "abbxxxxzzy"
s = "abc"
s = "aaa"
print(a.largeGroupPositions(s))	
						
		


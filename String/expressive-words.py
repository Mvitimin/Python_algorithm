
from typing import List
import collections

class Solution:
	def expressiveWords(self, S: str, words: List[str]) -> int:
		start = ans = 0
		if len(S) == 0:
			return ans
		
		def getGroups(S: str) -> List:
			stack = []
			for c in S:
				if stack and stack[-1][0] == c:
					stack[-1][1] += 1
				else:
					stack.append([c, 1])
			return stack
		
		base = getGroups(S)
		for word in words:
			comp = getGroups(word)
			if len(comp) == len(base):
				is_possible = True
				for i in range(len(base)):
					if comp[i][0] != base[i][0]:
						is_possible = False
						break
					elif comp[i][1] != base[i][1]:
						if comp[i][1] < base[i][1] and base[i][1] >= 3:
							continue
						is_possible = False
						break
				if is_possible:
					ans += 1
		return ans
						
						
a = Solution()
S = "heeellooo"
words = ["hello", "hi", "helo"]
'''
S = "aabbcfffooosss"
words = ["aabbc", "dfddd", "fffos"]
'''
print(a.expressiveWords(S, words))			

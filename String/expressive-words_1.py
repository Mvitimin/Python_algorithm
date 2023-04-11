
from typing import List
import itertools


class Solution:
	def expressiveWords(self, S: str, words: List[str]) -> int:
		start = ans = 0
		if len(S) == 0:
			return ans
		
		def getGroups(S: str) -> List:
			z = zip(*[(c, len(list(grp))) for c, grp in itertools.groupby(S)])
			return list(z)
		
		base = getGroups(S)
		for word in words:
			comp = getGroups(word)
			if base[0] != comp[0]:
				continue
			ans += all([c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(base[1], comp[1])])
		
		return ans
						
						
a = Solution()
S = "heeellooo"
words = ["hello", "hi", "helo"]
'''
S = "aabbcfffooosss"
words = ["aabbc", "dfddd", "fffos"]
'''
print(a.expressiveWords(S, words))			

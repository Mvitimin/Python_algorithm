import collections
from typing import List

class Solution:
	def findRepeatedDnaSequences(self, s: str) -> List[str]:
		n = len(s)
		seen = collections.defaultdict(int)
		bitmask = 0
		L = 10
		bit = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
		ans = []
		for i in range(n):
			if i >= L:
				bitmask <<= 2
				bitmask |= bit[s[i]]
				bitmask &= ~(3 << 2 * L)
			else:
				bitmask <<= 2
				bitmask |= bit[s[i]]
			if i >= L - 1:
				print(bin(bitmask))
				if bitmask in seen:
					ans.append(s[i - L + 1:i + 1])
					
		return ans	
			
a = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#s = "AAAAAAAAAAAAA"
print(a.findRepeatedDnaSequences(s))			

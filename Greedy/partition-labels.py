from typing import List
import collections
class Solution:
	def partitionLabels(self, S: str) -> List[int]:
		n = len(S)
		letters = collections.defaultdict(int)
		groups = collections.defaultdict(int) 	 	
		group, seen = 0, set()
		for i, c in enumerate(S):	
			index = i
			if c in seen:
				continue
			seen.add(c)
			for j in range(i, n):
				if S[j] == c:
					index = j
			if c in letters:
				group = letters[c]
			else:
				group += 1 
			for k in range(i, index + 1):
				letters[S[k]] = group 
		for c in S:
			groups[letters[c]] += 1
		return list(groups.values())
	
a = Solution()
s = "ababcbacadefegdehijhklij"
#s = "eccbbbbdec"
print(a.partitionLabels(s))				
		
					
					

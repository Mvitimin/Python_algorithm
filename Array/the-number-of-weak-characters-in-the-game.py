from typing import List
from functools import cmp_to_key

class Solution:
	def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
		n = len(properties)	
		def compare(x, y):
			if x[0] == y[0]:
				return y[1] - x[1]
			else:
				return x[0] - y[0]
		
		properties.sort(key=cmp_to_key(compare))
		
		max_defense = 0
		ans = 0 
		for i in range(n - 1, -1, -1):
			if max_defense > properties[i][1]:
				ans += 1
			max_defense = max(max_defense, properties[i][1])
		
		return ans
			
a = Solution()
properties = [[5,5],[6,3],[3,6]]
properties = [[2,2],[3,3]]
properties = [[1,5],[10,4],[4,3]]
properties = [[1,1],[2,1],[2,2],[1,2]]
properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]]
properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
print(a.numberOfWeakCharacters(properties))

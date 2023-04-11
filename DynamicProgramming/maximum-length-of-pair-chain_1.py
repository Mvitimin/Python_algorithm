from typing import List

class Solution:
	def findLongestChain(self, pairs: List[List[int]]) -> int:
		n = len(pairs)
		pairs.sort(key=lambda x : x[1])
		start = float('-inf')
		ans = n
		for x, y in pairs:
			if x <= start:
				ans -= 1
			else: start = y
		return ans
		
a = Solution()
pairs = [[1,2],[2,3],[3,4]]
pairs = [[1,2],[7,8],[4,5]]
print(a.findLongestChain(pairs))


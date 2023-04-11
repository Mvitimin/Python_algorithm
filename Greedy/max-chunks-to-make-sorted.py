from typing import List

class Solution:
	def maxChunksToSorted(self, arr: List[int]) -> int:
		res = end = 0
		for i, n in enumerate(arr):
			end = max(end, n)
			if end == i:
				res += 1
				end = i + 1
		return res

a = Solution()

#arr = [1, 0, 2, 3, 4]
arr = [4, 3, 2, 1, 0]
print(a.maxChunksToSorted(arr))
			


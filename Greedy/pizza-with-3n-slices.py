from typing import List
from functools import lru_cache

class Solution:
	def maxSizeSlices(self, slices: List[int]) -> int:
		n = len(slices)
		cur1 = cur2 = 0
		tmp = prev = 0
		nums = slices 
		if len(nums) <= 1: return sum(nums)
		
		n = len(nums)
		for i in range(n - 1):
			cur1 = max(tmp + nums[i], prev)
			tmp, prev = prev, cur1

		tmp = prev = 0 			
		for i in range(1, n):
			cur2 = max(tmp + nums[i], prev)
			tmp, prev = prev, cur2
		return max(cur1, cur2)
		

'''
class Solution:
	def maxSizeSlices(self, slices: List[int]) -> int:
		n = len(slices)
		need = n // 3
		@lru_cache(None)
		def solve(i, j, k):
			if k == 1: return max(slices[i:j + 1])
			if (j - i + 1) < 2 * k - 1: return float('-inf')
			return max(slices[i] + solve(i + 2, j, k - 1), solve(i + 1, j, k))
		return max(solve(0, n - 2, need), solve(1, n - 1, need))
'''			


a = Solution()
slices = [1, 2, 3, 4, 5, 6]
slices = [8,9,8,6,1,1]
#slices = [6,3,1,2,6,2,4,3,10,4,1,4,6,5,5,3,4,7,6,5,8,7,3,8,8,1,7,1,7,8]
print(a.maxSizeSlices(slices))

from typing import List
class Solution:
	def find132pattern(self, nums: List[int]) -> bool:
		
		n = len(nums)
		if n < 3:
			return False
		
		min_idx = []
		maxs = []
		
		for i, num in enumerate(nums):
			if not min_idx or nums[min_idx[-1]] > num:
				min_idx.append(i)
		
		for i in range(n - 1, -1, -1):
			while min_idx and min_idx[-1] >= i:
				min_idx.pop()
			
			while maxs and min_idx and maxs[-1] <= nums[min_idx[-1]]:
				maxs.pop()
			
			if min_idx and maxs and nums[i] > maxs[-1]:
				return True
			
			maxs.append(nums[i])
				
		return False	
			
a = Solution()
nums = [1, 2, 3, 4]
nums = [3, 1, 4, 2]
#nums = [-1, 3, 2, 0]
nums = [1,-4,2,-1,3,-3,-4,0,-3,-1]
print(a.find132pattern(nums))			

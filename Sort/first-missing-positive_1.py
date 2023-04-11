from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		i, n = 0, len(nums)
		
		while i < n:
			k = nums[i] - 1
			if 0 <= k < n and nums[k] != k + 1:
				nums[i], nums[k] = nums[k], nums[i]
			else:
				i += 1
		
		for i in range(n):
			if nums[i] != i + 1:
				return i + 1
				
		return n + 1				
			

a = Solution()
nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
print(a.firstMissingPositive(nums))

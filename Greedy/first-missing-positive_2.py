from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		n = len(nums)
		if 1 not in nums:
			return 1
		
		for i in range(n):
			if nums[i] > n or nums[i] <= 0:
				nums[i] = 1
		
		for i in range(n):
			idx = abs(nums[i]) - 1
			if nums[idx] > 0:
				nums[idx] *= -1
		
		for i in range(n):
			if nums[i] > 0:
				return i + 1
		
		return n + 1
	
a = Solution()
nums = [1, 2, 0]
nums = [3, 4, -1, 1]
print(a.firstMissingPositive(nums))				
					
		
			

from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]):
		n = len(nums)
		if 1 not in nums:
			return 1
			
		for i in range(n):
			if nums[i] <= 0 or nums[i] > n:
				nums[i] = 1
				
		for i in range(n):
			k = abs(nums[i])
			nums[k - 1] = -abs(nums[k - 1])
		
		for i in range(n):
			if nums[i] > 0:
				return i + 1
		return n + 1
				
			
a = Solution()
nums = [1, 2, 0]
#nums = [3, 4, -1, 1]
#nums = [7, 8, 9, 11, 12]
#nums = [3, 4, 1, 2]
print(a.firstMissingPositive(nums))			
				
				
						
			


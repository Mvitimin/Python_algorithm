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
			k = abs(nums[i])
			if k == n:
				nums[0] = -abs(nums[0])
			else:
				nums[k] = -abs(nums[k])
		
		for i in range(1, n):
			if nums[i] > 0: return i 
		if nums[0] > 0: return n 
		return n + 1	

a = Solution()
nums = [1,2,0]
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
print(a.firstMissingPositive(nums))

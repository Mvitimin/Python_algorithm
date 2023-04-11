from typing import List

class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		seen = dict()
		s = 0
		for i, num in enumerate(nums):
			s += nums[i]
			val = s % k
			if i >= 1 and val == 0: return True
			if val in seen and seen[s % k] < i - 1:
				return True	
			if val not in seen: seen[val] = i
		return False
						
a = Solution()
nums = [23,2,4,6,7]; k = 6			
nums = [23,2,6,4,7]; k = 6	
nums = [23,2,6,4,7]; k = 13			
print(a.checkSubarraySum(nums, k))
		
			

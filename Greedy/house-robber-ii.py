from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		
		cur1 = cur2 = 0
		tmp = prev = 0 
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
		
a = Solution()
nums = [2, 3, 2]
nums = [1,2,3,1]
nums = [1,2,3]
print(a.rob(nums))
			

from typing import List

class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		n = len(nums)	
		s = val = cur = 0 
		ans = float('-inf')	
		minVal = float('inf')
		for i in range(n):
			s += nums[i]
			cur = max(nums[i], cur + nums[i])
			val = min(nums[i], val + nums[i])
			minVal = min(val, minVal)
			ans = max(ans, cur)			
		return max(ans, s - minVal) if minVal != val else ans

a = Solution()
nums = [1,-2,3,-2]
#nums = [-3,-2,-3]
nums = [5,-3,5]
#nums = [-5, 3, 5]
print(a.maxSubarraySumCircular(nums))

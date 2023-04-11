from typing import List
class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		
		min_sum = 0
		sum_val = 0
		ans = nums[0]
		for i in range(len(nums)):
			sum_val += nums[i]
			ans = max(ans, sum_val - min_sum)
			min_sum = min(sum_val, min_sum)
		return ans

a = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
nums = [-1]
print(a.maxSubArray(nums))

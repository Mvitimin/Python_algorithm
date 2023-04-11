from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		ans = prev_sum = nums[0]
		
		for i in range(1, len(nums)):
			prev_sum = max(prev_sum + nums[i], nums[i])				
			ans = max(ans, prev_sum)
		
		return ans	
		
a = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(a.maxSubArray(nums))

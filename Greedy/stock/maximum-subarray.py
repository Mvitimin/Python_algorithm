from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		ans = nums[0]
		for i in range(1, len(nums)):
			nums[i] = max(nums[i], nums[i] + nums[i - 1])
			ans = max(ans, nums[i])
		return ans

a = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
nums = [5,4,-1,7,8]
print(a.maxSubArray(nums))
			


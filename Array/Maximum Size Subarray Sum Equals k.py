from typing import List


class Solution:
	def maxSubArrayLen(self, nums: List[int], k: int) -> int:
		
		pre_sum = dict()
		val = 0
		pre_sum[0] = -1
		ans = 0
		
		
		for i, num in enumerate(nums):
			val += num
			if val - k in pre_sum:
				ans = max(ans, i - pre_sum[val - k])
			if val not in pre_sum:
				pre_sum[val] = i
		return ans	

a = Solution()
nums = [1,-1,5,-2,3]; k = 3
nums = [-2,-1,2,1]; k = 1
print(a.maxSubArrayLen(nums, k))

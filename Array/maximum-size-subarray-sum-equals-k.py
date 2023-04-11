from typing import List

class Solution:
	def maxSubArrayLen(self, nums: List[int], k: int) -> int:
		map = {0: -1}
		s = 0
		ans = 0
		for i, n in enumerate(nums):
			s += nums[i]
			
			if s - k in map:
				ans = max(ans, i - map[s - k])
			
			if s not in map:
				map[s] = i 
		return ans
			
a = Solution()
nums = [1,-1,5,-2,3]; k = 3
nums = [-2,-1,2,1]; k = 1
print(a.maxSubArrayLen(nums, k))

from typing import List
from functools import lru_cache
class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		n = len(nums)
		@lru_cache(None)
		def dp(i, p):
			if i == n:
				if p == target:
					return 1 
				else: return 0 
			return dp(i + 1, p - nums[i]) + dp(i + 1, p + nums[i])
		return dp(0, 0)	
		
a = Solution()
nums = [1,1,1,1,1]; target = 3

#nums = [1]; target = 1
print(a.findTargetSumWays(nums, target))
			


from typing import List
from functools import lru_cache

class Solution:
	def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
		
		n, m = len(nums), len(multipliers)
		
		@lru_cache(2000)
		def dp(k, i):
			j = n + i - 1 - k 
			if i > j or k >= m: return 0
			return max(nums[i] * multipliers[k] + dp(k + 1, i + 1), nums[j] * multipliers[k] + dp(k + 1, i))
		
		return dp(0, 0)
		

				
a = Solution()
nums = [1,2,3]; multipliers = [3,2,1]
#nums = [-5,-3,-3,-2,7,1]; multipliers = [-10,-5,3,4,6]
print(a.maximumScore(nums, multipliers))

from typing import List
from functools import lru_cache

class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)
		
		@lru_cache(None)	
		def dp(i, prev, start):
			if i == n:
				return 0 		
			res = float('-inf')
			if (i == n - 1 and not (prev or start)) or (i < n - 1 and not prev):
				res = max(res, nums[i] + dp(i + 1, True, start if i != 0 else True))
			res = max(res, dp(i + 1, False, start))
			return res		
		return dp(0, False, False)
					
			
a = Solution()
nums = [2,3,2]
nums = [1,2,3,1]
#nums = [1,2,3]
print(a.rob(nums))			


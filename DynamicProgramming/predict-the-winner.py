from typing import List
from functools import lru_cache

class Solution:
	def PredictTheWinner(self, nums: List[int]) -> bool:
		s = sum(nums)
		@lru_cache(None)
		def dp(i, j):
			if j - i + 1 <= 0:
				return 0
			return max(nums[i] - dp(i + 1, j),
			nums[j] - dp(i, j - 1))
			
		return dp(0, len(nums) -1) >= 0 	


a = Solution()
#nums = [1,5,2]
nums = [1,5,233,7]
print(a.PredictTheWinner(nums))


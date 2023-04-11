from typing import List
from functools import lru_cache
class Solution:
	def combinationSum4(self, nums: List[int], target: int) -> int:
		@lru_cache(None)
		def combination(res):
			if res == 0:
				return 1 
			ans = 0
			for n in nums:
				if res - n >= 0:
					ans += combination(res - n)
			return ans	
		return combination(target)
		
a = Solution()
nums = [1,2,3]; target = 4			
#nums = [9]; target = 3	
print(a.combinationSum4(nums, target))


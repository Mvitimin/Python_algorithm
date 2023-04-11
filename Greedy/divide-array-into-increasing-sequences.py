import collections
from typing import List

class Solution:
	def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
		return (len(nums) // max(collections.Counter(nums).values())) >= k		
		
		
a = Solution()
nums = [1,2,2,3,3,4,4]; k = 3
print(a.canDivideIntoSubsequences(nums, k))

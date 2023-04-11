from typing import List
class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		index_map = {}
		
		for i, num in enumerate(nums):
			if num in index_map:
				diff = i - (index_map[num])
				if diff <= k:
					return True
			index_map[num] = i
		return False

		
a = Solution()
nums = [1,2,3,1]; k = 3
nums = [1,0,1,1]; k = 1
nums = [1,2,3,1,2,3]; k = 2
print(a.containsNearbyDuplicate(nums, k))

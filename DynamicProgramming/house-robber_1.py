from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		cur, prevp, prev = 0, 0, 0
		for i in range(len(nums)):
			cur = max(prev, prevp + nums[i])
			prev, prevp = cur, prev
		return cur
		
a = Solution()
nums = [2,1,1,2]
#nums = []
#nums = [1, 2, 3, 1]
print(a.rob(nums))

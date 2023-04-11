from typing import List
import collections

class Solution:
	def canJump(self, nums: List[int]) -> bool:
		if len(nums) < 2:
			return True
		q = collections.deque([0])
		start, end = 1, 1
		while q:
			index = q.popleft()		
			end = index + nums[index] + 1 
			for next in range(start, end):
				if next >= len(nums) - 1 or nums[next] + next >= len(nums) - 1:
					return True
				q.append(next)
			start = end			
		return False
		
				
nums = [2,3,1,1,4]		
nums = [3,2,1,0,4]
nums = [3,3,1,2,5,6,7,8,9,1,2,3,4]
a = Solution()
print(a.canJump(nums))

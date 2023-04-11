from typing import List
class Solution:
	def jump(self, nums: List[int]) -> int:
		if len(nums) <= 1:
			return 0
		farthest = jump = 0
		end = 0 
		for i in range(len(nums) - 1):
			farthest = max(farthest, nums[i] + i)
			if i == end:
				jump += 1
				end = farthest				
		return jump
			
			


a = Solution()
#nums = [2,3,1,1,4]
#nums = [2,3,0,1,4]
nums = [1,1,1,1]
print(a.jump(nums))

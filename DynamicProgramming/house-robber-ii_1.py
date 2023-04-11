from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)
		if n == 1:
			return nums[0]
		cur1 = cur2 = 0
		prev = temp = 0
		for i in range(n - 1):
			cur1 = max(temp + nums[i], prev)
			temp, prev = prev, cur1
		prev = temp = 0
		for i in range(1, n):
			cur2 = max(temp + nums[i], prev)
			temp, prev = prev, cur2	
		return max(cur1, cur2)	
							
a = Solution()
nums = [2,3,2]
#nums = [1,2,3,1]
#nums = [1,2,3]
print(a.rob(nums))			

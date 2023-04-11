from typing import List
class Solution:
	def rob(self, nums: List[int]) -> int:
		n = len(nums)
		if n <= 2:
			return max(nums)
		
		pprev, prev = 0, nums[1] 
		cur = 0
		for i in range(2, n):
			cur = max(pprev + nums[i], prev)
			pprev, prev = prev, cur
		
		ans = cur 
		
		pprev, prev = 0, nums[0] 
		cur = 0
		
		for i in range(1, n - 1):
			cur = max(pprev + nums[i], prev)
			pprev, prev = prev, cur
		ans = max(cur, ans)
		return ans	
				
a = Solution()
nums = [2, 3, 2]
nums = [1, 2, 3, 1]
nums = [1, 2, 3]
print(a.rob(nums))			

from typing import List

class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		tortoise = hare = nums[0]
		
		while True:
			tortoise, hare = nums[tortoise], nums[nums[hare]]
			if tortoise == hare:
				break
		
		tortoise = nums[0]
		while tortoise != hare:
			tortoise, hare = nums[tortoise], nums[hare]
		return hare
			
		
a = Solution()
nums = [1,3,4,2,2]
#nums = [3,1,3,4,2]
#nums = [2,2,2,2,2]
print(a.findDuplicate(nums))

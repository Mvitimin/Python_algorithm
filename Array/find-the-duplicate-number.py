from typing import List

class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		hare = tortoise = 0
		while True:
			hare = nums[nums[hare]]
			tortoise = nums[tortoise]
			if hare == tortoise:
				break
		tortoise = 0
		while hare != tortoise:
			hare = nums[hare]
			tortoise = nums[tortoise]
		return hare
			
		
				
a = Solution()
nums = [3,1,3,4,2]
#nums = [1,3,4,2,2]
#nums = [1,1,2]
print(a.findDuplicate(nums))

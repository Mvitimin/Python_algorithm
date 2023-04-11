from typing import List

class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		ans = []
		i = 0
		n = len(nums)
		for i in range(n):
			new_index = abs(nums[i]) - 1
			if nums[new_index] > 0:
				nums[new_index] *= -1
		
		return [i + 1 for i in range(n) if nums[i] > 0]		
			
a = Solution()
nums = [4,3,2,7,8,2,3,1]
#nums = [1, 2, 2, 5, 5]
print(a.findDisappearedNumbers(nums))	
	

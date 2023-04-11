from typing import List

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		n = len(nums)
		k = i = 0
		j = n - 1
		
		while i <= j:
			if nums[i] == 0:
				nums[k], nums[i] = nums[i], nums[k]
				i += 1
				k += 1
			elif nums[i] == 2:
				nums[i], nums[j] = nums[j], nums[i]
				j -= 1
			else:
				i += 1
						
		return nums

a = Solution()
#nums = [2,0,2,1,1,0]
nums = [1, 0, 2]
nums = [0,2,2,2,0,2,1,1]
nums = [1,2,1,2]
nums = [2,2,0,0,2,0,1,2,0,2]
print(a.sortColors(nums))
		


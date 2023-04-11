from typing import List

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		n = len(nums)
		i, j = 0, n - 1
		k = 0
		
		while k <= j:
			if nums[k] < 1:
				nums[i], nums[k] = nums[k], nums[i]
				i += 1
				k += 1
			elif nums[k] > 1:
				nums[j], nums[k] = nums[k], nums[j]	
				j -= 1
			else:
				k += 1
		#print(nums)
			
a = Solution()
nums = [2,0,2,1,1,0]
nums = [0, 0, 1, 2, 0, 1, 2]
nums = [2, 0, 1]
print(a.sortColors(nums))

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
				nums[k], nums[j] = nums[j], nums[k]
				j -= 1
			else:
				k += 1
a = Solution()
nums = [2, 0, 2, 1, 1, 0]
nums = [2, 0, 1]
nums = [1, 1, 0, 2, 1, 0, 2, 0]
nums = [1, 2, 2, 0]
a.sortColors(nums)


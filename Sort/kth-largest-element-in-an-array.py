from typing import List
import random

class Solution:
	def partition(self, l, r, nums: List[int]):
		i, p = l, random.randint(l, r)
		pivot = nums[p]
		nums[r], nums[p] = nums[p], nums[r] 
		for j in range(l, r):
			if nums[j] <= pivot:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
		nums[i], nums[r] = nums[r], nums[i]
		return i		
	
	def quickSelect(self, l, r, k, nums: List[int]):
		index = 0
		while l <= r:
			index = self.partition(l, r, nums)
			if index == k:
				break
			elif index > k:
				r = index - 1
			else:
				l = index + 1
		return nums[index]
				
	
	def findKthLargest(self, nums: List[int], k: int) -> int:
		n = len(nums)
		return self.quickSelect(0, n - 1, n - k, nums)
		
a = Solution()
nums = [3,2,1,5,6,4]; k = 2
#nums = [3,2,3,1,2,4,5,5,6]; k = 4
print(a.findKthLargest(nums, k))

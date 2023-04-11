from typing import List
import random	
class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		n = len(nums)
		
		def partition(l, r):
			mid = random.randint(l, r)
			i, pivot = l, nums[mid]
			nums[r], nums[mid] = nums[mid], nums[r]
				
			for j in range(l, r):
				if nums[j] <= pivot:
					nums[i], nums[j] = nums[j], nums[i]
					i += 1
			nums[i], nums[r] = nums[r], nums[i]
			return i
		
		l, r = 0, n - 1
		
		while l <= r:
			i = partition(l, r)
			if i == n - k:
				break
			elif i > n - k:
				r = i - 1
			else:
				l = i + 1
		return nums[i]					
			
		
				
			
		
		
a = Solution()
nums = [3,2,1,5,6,4]; k = 2
#nums = [3,2,3,1,2,4,5,5,6]; k = 4
#nums = [5,2,4,1,3,6,0]; k = 4
#nums = [-1,2,0]; k = 2
print(a.findKthLargest(nums, k))



from typing import List
class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		n = len(nums)
		if n == 1:
			return 
		if nums[-1] > nums[-2]:
			nums[-1], nums[-2] = nums[-2], nums[-1]
			return 
		
		for i in range(n - 2, -1, -1):
			if nums[i] >= nums[i + 1]:
				continue
			else:
				val, index = nums[i + 1], i + 1
				for j in range(i + 2, n):
					if nums[j] > nums[i] and val >= nums[j]:
						val, index = nums[j], j
				nums[i], nums[index] = nums[index], nums[i]
				break
		else: i = -1
		
		left, right = i + 1, n - 1
		while left < right and nums[right] < nums[left]:
			nums[right], nums[left] = nums[left], nums[right]
			left += 1
			right -= 1
		#print(nums)
		
a = Solution()
arr = [2, 3, 4, 1, 5, 6]
arr = [2,3,1,3,3]
arr = [2,1,2,2,2,2,2,1]
#arr = [3, 2, 1]
#arr = [1, 2, 3, 6, 4, 3, 2]
#arr = [1, 1, 5]
#arr = [3, 2, 1]
a.nextPermutation(arr)
				
						 
					
						
						
						
						
						
						
					
				
					
				 
			
			

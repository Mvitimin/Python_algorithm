from typing import List

class Solution:
	def findUnsortedSubarray(self, nums: List[int]) -> int:
		n = len(nums)	
		small, big = float('inf'), float('-inf')
		s = e = 0 
		for i in range(1, n):
			if nums[i - 1] > nums[i] and nums[i] < small:
				small, s = nums[i], i 
			if nums[i - 1] > nums[i] and nums[i - 1] > big:
				big, e = nums[i - 1], i - 1
		for i in range(s + 1):
			if nums[i] > small:
				s = i 
				break
		for i in range(n - 1, e - 1, -1):
			if nums[i] < big:
				e = i
				break
		return e - s + 1 if s < e else 0		
				
					
			
					
				
		
		
										
a = Solution()
#nums = [2,6,4,8,10,9,15]
#nums = [1, 2, 3, 4]
nums = [1,3,2,2,2]
#nums = [1]
print(a.findUnsortedSubarray(nums))			


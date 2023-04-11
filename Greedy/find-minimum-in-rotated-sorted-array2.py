from typing import List

class Solution:
	def findMin(self, nums: List[int]) -> int:
		
		n = len(nums)
		l, r = 0, n - 1
		
		if n == 1 or nums[0] < nums[-1]:
			return nums[0]
				
		while l <= r:
			
			mid = l + (r - l) // 2
			
			if nums[mid] > nums[-1]:
				l = mid + 1		
			else:
				if mid > 0 and nums[mid - 1] > nums[mid]:
					return nums[mid]
				else:
					r = mid - 1								

a = Solution()
nums = [3, 4, 5, 1, 2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]
print(a.findMin(nums))	
					
				
					
				
				


from typing import List

class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		
		for i in range(len(nums)):
			j = i
			while j != nums[j] - 1:
				if nums[nums[j] - 1] == nums[j]:
					return nums[j]
				tmp, nums[nums[j] - 1] = nums[nums[j] - 1], nums[j]
				nums[j] = tmp
		return 1	

a = Solution()
nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(a.findDuplicate(nums))
				
				
			
		
		


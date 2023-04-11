from typing import List

class Solution:
	def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
		start = lower - 1
		ans = []
		nums.append(upper + 1)
		for i in range(len(nums)):
			if nums[i] != start + 1:
				ans.append("{}->{}".format(start + 1, nums[i] - 1) if start + 1 != nums[i] - 1 else str(start + 1))
			start = nums[i]
		return ans		
				
a = Solution()			
nums = [0,1,3,50,75]; lower = 0; upper = 99	
nums = []; lower = 1; upper = 1	
nums = []; lower = -3; upper = -1
nums = [-1]; lower = -1; upper = -1
nums = [-1]; lower = -2; upper = -1
nums = [0,1,3,50,99]; lower = 0; upper = 99	
print(a.findMissingRanges(nums, lower, upper))

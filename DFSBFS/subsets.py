from typing import List

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		
		ans = []
		def solve(start, comb):
			ans.append(comb)
			if len(comb) >= len(nums):
				return 
			for i in range(start, len(nums)):
				solve(i + 1, comb + [nums[i]])
		solve(0, [])
		return ans
		
a = Solution()	
nums = [0]
print(a.subsets(nums))
				


from typing import List

class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		
		nums.sort()
		n = len(nums)
		
		ans = []
		tmp = []
		
		def solve(i):
			ans.append(tmp[:])
			
			for j in range(i, n):
				if j > i and nums[j - 1] == nums[j]:
					continue
				tmp.append(nums[j])
				solve(j + 1)
				tmp.pop()
			
		solve(0)
		return ans	

	
a = Solution()
nums = [1, 2, 2]
#nums = [0]
#nums = [1, 2, 2, 3, 3]
print(a.subsetsWithDup(nums))	
					
			
			
			
			

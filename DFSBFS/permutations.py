from typing import List

class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		ans, tmp = [], []
		visited = [0] * len(nums)
		def solve():	
			if len(tmp) == len(nums):
				ans.append(tmp[:])				
			for i in range(len(nums)):
				if not visited[i]:
					tmp.append(nums[i])
					visited[i] = 1
					solve()
					tmp.pop()
					visited[i] = 0
		solve()
		return ans


a = Solution()
#nums = [1,2,3]
nums = [0, 1]
print(a.permute(nums))
					
					
					
			
		

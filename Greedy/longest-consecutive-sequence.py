from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		seen = set(nums)
		visited = {}
		
		def dfs(num):	
			if num in seen:
				visited[num] = dfs(num + 1) + 1
				seen.remove(num)
			return visited[num] if num in visited else 0 
		
		ans = 0
		for num in nums:
			if num in seen:
				dfs(num)
				ans = max(ans, visited[num])				
		return ans

a = Solution()
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(a.longestConsecutive(nums))			
		
		

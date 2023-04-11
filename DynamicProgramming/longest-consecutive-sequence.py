from typing import List
import collections

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums:
			return 0
			
		dp = {}
		nums_set = set(nums)
	
		def find(x):
			if x - 1 in nums_set:
				if x - 1 in dp:
					dp[x] = dp[x - 1] + 1
				else:
					dp[x] = find(x - 1) + 1
			else: dp[x] = 1
			return dp[x]
		for num in nums:
			find(num)	
		return max(dp.values())			
							
a = Solution()
nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [6, 3, 1, 5, 2, 9, 7, 4]
print(a.longestConsecutive(nums))

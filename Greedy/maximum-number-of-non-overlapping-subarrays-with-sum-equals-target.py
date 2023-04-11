from typing import List


class Solution:
		
	def maxNonOverlapping(self, nums: List[int], target: int) -> int:	
		n = len(nums)
		dp = [0] * (n + 1) 
		s = 0
		index_map = {0: 0}
		index_map[0] = 0
					
		for i in range(1, n + 1):
			s += nums[i - 1]
			find = s - target
			if find in index_map:
				dp[i] = max(dp[i], dp[index_map[find]] + 1)
			dp[i] = max(dp[i], dp[i - 1])
			index_map[s] = i	
		return dp[-1]

a = Solution()
arr = [1, 2, 3, 3, 3, 3, 4]
arr = [-2, 0, 4]

nums = [1,1,1,1,1]; target = 2
#nums = [-1,3,5,1,4,2,-9]; target = 6
nums = [-2,6,6,3,5,4,1,2,8]; target = 10
#nums = [0, 0, 0]; target = 0
print(a.maxNonOverlapping(nums, target))


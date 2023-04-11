
from typing import List

class Solution:
	def splitArray(self, nums: List[int], m: int) -> int:
		s, n = sum(nums), len(nums)
		dp = [[s for j in range(m)] for i in range(n)]
		
		sum_map = [[0 for j in range(n)] for i in range(n)]
		
		for i in range(n):
			sum_map[i][i] = nums[i]
			for j in range(i + 1, n):
				sum_map[i][j] = sum_map[i][j - 1] + nums[j]
				
		for i in range(1, n):
			dp[i][0] = s - nums[i - 1]
			s -= nums[i - 1]
		for j in range(1, m):
			for i in range(n):
				for k in range(i + 1, n):
					dp[i][j] = min(max(sum_map[i][k - 1], dp[k][j - 1]), dp[i][j])
		return dp[0][-1]
nums = [1, 2, 3, 4, 5]; m = 3
a = Solution()
print(a.splitArray(nums, m))
				


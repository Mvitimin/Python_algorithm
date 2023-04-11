from typing import List
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		dp, n = {}, len(nums)
		def solve(prev):
			if prev == n - 1:
				return 1
			if prev in dp:
				return dp[prev]
			dp[prev] = 1
			for i in range(prev + 1, n):
				if nums[prev] < nums[i]:
					dp[prev] = max(dp[prev], 1 + solve(i))
			return dp[prev]
		return max([solve(i) for i in range(n)])
				
			
a = Solution()
#nums = [10,9,2,5,3,7,101,18]
#nums = [0,1,0,3,2,3]
#nums = [7,7,7,7,7,7,7]
nums = [0, 8, 4, 12, 2]
print(a.lengthOfLIS(nums))

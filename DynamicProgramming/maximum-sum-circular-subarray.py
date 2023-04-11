from typing import List

class Solution:
	def maxSubarraySumCircular(self, nums: List[int]) -> int:
		n = len(nums)	
		cur, ans = 0, float('-inf')
		dp = [0] * (n + 1) 
		s, val = sum(nums), float('-inf')
		for i in range(n):
			dp[i] = dp[i - 1] + nums[i]
			val = max(dp[i], val)
			ans = max(ans, s - dp[i] + val)
			cur = max(nums[i], cur + nums[i])
			ans = max(ans, cur)			
		return ans

a = Solution()
nums = [1,-2,3,-2]
#nums = [-3,-2,-3]
#nums = [5,-3,5]
#nums = [-5, 3, 5]
print(a.maxSubarraySumCircular(nums))


from typing import List

class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		n = len(nums)
		dp = [1] * n 
		ans = 1
		for i in range(n):
			for j in range(i):
				if nums[i] > nums[j]:
					dp[i] = max(dp[i], dp[j] + 1)
			ans = max(ans, dp[i])
		return ans 


a = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
nums = [7,7,7,7,7,7,7]
print(a.lengthOfLIS(nums))

				


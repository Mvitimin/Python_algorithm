from typing import List
import bisect
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		n = len(nums)
		dp = []
		for c in nums:
			i = bisect.bisect_left(dp, c)
			print(c, i)
			if i == len(dp):
				dp.append(c)
			else:
				dp[i] = c
			print(dp)
		return len(dp)
				
a = Solution()
#nums = [10,9,2,5,3,7,101,18]
#nums = [0,1,0,3,2,3]
#nums = [7,7,7,7,7,7,7]
nums = [0, 8, 4, 12, 2]
print(a.lengthOfLIS(nums))

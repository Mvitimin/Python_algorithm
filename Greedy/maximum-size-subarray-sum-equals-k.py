from typing import List

class Solution:
	def maxSubArrayLen(self, nums: List[int], k: int) -> int:
		seen = {0: -1}
		sums = 0
		ans = 0
		for i, num in enumerate(nums):
			sums += num 
			if sums - k in seen:
				ans = max(ans, i - seen[sums - k])
			if sums not in seen:
				seen[sums] = i
		return ans


a = Solution()
nums = [1,-1,5,-2,3]; k = 3
nums = [-2,-1,2,1]; k = 1
print(a.maxSubArrayLen(nums, k))

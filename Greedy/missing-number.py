from typing import List

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		ans = len(nums)
		for i, n in enumerate(nums):
			ans ^= i ^ n
		return ans
		
a = Solution()
nums = [3, 0, 1]
print(a.missingNumber(nums))
		

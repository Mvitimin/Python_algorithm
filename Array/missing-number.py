from typing import List

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		n = len(nums)
		s = n
		for i in range(n):
			s ^= (nums[i] ^ i)
			print(s)
		return s

a = Solution()
nums = [3,0,1]
print(a.missingNumber(nums))::

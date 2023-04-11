from typing import List
import bisect
class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		n = len(nums)
		sub = []
		for c in nums:
			index = bisect.bisect_left(sub, c)
			if index == len(sub):
				sub.append(c)
			else:
				sub[index] = c
		return len(sub)

a = Solution()
nums = [10,9,2,5,3,7,101,18]
#nums = [0,1,0,3,2,3]
#nums = [7,7,7,7,7,7,7]
print(a.lengthOfLIS(nums))


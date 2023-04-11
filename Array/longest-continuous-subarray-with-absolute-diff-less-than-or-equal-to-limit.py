# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
#solution https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/615407/Fast-solution-in-Python-(beats-greater-99)-and-more-with-explaination

from typing import List
from collections import deque

class Solution:
	def longestSubarray(self, nums: List[int], limit: int) -> int:
		start, ans = 0, 1	
		mins = deque([(float('inf'), 0)])
		maxs = deque([(float('-inf'), 0)])
		for i in range(len(nums)):
			while mins and mins[-1][0] > nums[i]:
				mins.pop()
			mins.append((nums[i], i))
			while maxs and maxs[-1][0] < nums[i]:
				maxs.pop()
			maxs.append((nums[i], i))
			while maxs[0][0] - mins[0][0] > limit and start < i:
				if maxs[0][1] <= start: maxs.popleft()
				if mins[0][1] <= start: mins.popleft()
				start += 1
			ans = max(ans, i - start + 1)
						
		return ans	
			
a = Solution()'""'
#nums = [10,1,2,4,7,2]
#nums = [4,2,2,2,4,4,2,2]
#limit = 0
#nums = [8,2,4,7]
#limit = 4
nums = [1,5,6,7,8,10,6,5,6]
limit = 4
print(a.longestSubarray(nums, limit)) 


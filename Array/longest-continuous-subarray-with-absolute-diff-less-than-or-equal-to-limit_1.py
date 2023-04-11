# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
#solution https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/615407/Fast-solution-in-Python-(beats-greater-99)-and-more-with-explaination

from typing import List
from collections import deque

class Solution:
	def longestSubarray(self, nums: List[int], limit: int) -> int:
		mins, maxs = deque([]), deque([])
		ans, start = 1, 0
		
		for i in range(len(nums)):
			while mins and nums[i] < mins[-1][0]:
				mins.pop()
			mins.append((nums[i], i))
			while maxs and nums[i] > maxs[-1][0]:
				maxs.pop()
			maxs.append((nums[i], i))
			
			while start < i and maxs[0][0] - mins[0][0] > limit:
				if mins[0][1] <= start:
					mins.popleft()
				if maxs[0][1] <= start:
					maxs.popleft()
				start += 1
			print(nums[start:i+1])
			ans = max(ans, i - start + 1)
		return ans	
			
a = Solution()
#nums = [10,1,2,4,7,2]
#nums = [4,2,2,2,4,4,2,2]
#limit = 0
#nums = [8,2,4,7]
#limit = 4
nums = [1,5,6,7,8,10,6,5,6]
limit = 4
print(a.longestSubarray(nums, limit)) 

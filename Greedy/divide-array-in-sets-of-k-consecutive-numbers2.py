# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
from typing import List
import collections
class Solution:
	def isPossibleDivide(self, nums: List[int], k: int) -> bool:
		if len(nums) % k != 0:
			return False
		
		counter = collections.Counter(nums)
		for num in sorted(counter.keys()):
			if counter[num] <= 0:
				continue
			for i in range(1, k):
				if counter[num + i] < counter[num]:
					return False
				counter[num + i] -= counter[num]
							
		return True
		

a = Solution()
nums = [1,2,3,3,4,4,5,6]
k = 4
#nums = [3,3,2,2,1,1]
#k = 3
#nums = [3,2,1,2,3,4,3,4,5,9,10,11]
#k = 3

#nums = [1,1,2,2,3,3]
#k = 2

print(a.isPossibleDivide(nums, k))
		

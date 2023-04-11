# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
from typing import List
import collections
class Solution:
	def isPossibleDivide(self, nums: List[int], k: int) -> bool:
		if len(nums) % k != 0:
			return False
		length = len(nums) // k
		cnts = [[] for i in range(len(nums) // k)] 
		count_map = collections.defaultdict(int)
		for i in nums:
			count_map[i] += 1
		
		for i in sorted(set(nums)):
			index = 0
			while index < length and count_map[i] > 0:
				if len(cnts[index]) < k and (not cnts[index] or i - cnts[index][-1] == 1):
					count_map[i] -= 1
					cnts[index].append(i)
				index += 1
			if count_map[i] != 0:
				return False
		
		return True
		

a = Solution()
#nums = [1,2,3,3,4,4,5,6]
#k = 4
#nums = [3,3,2,2,1,1]
#k = 3
#nums = [3,2,1,2,3,4,3,4,5,9,10,11]
#k = 3

#nums = [1,1,2,2,3,3]
#k = 2

print(a.isPossibleDivide(nums, k))
		

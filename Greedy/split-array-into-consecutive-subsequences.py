import collections
from typing import List
class Solution:
	def isPossible(self, nums: List[int]) -> bool:
		counter = collections.Counter(nums)
		end = collections.defaultdict(int)
		for n in nums:
			if not counter[n]: continue
			counter[n] -= 1
			if end[n - 1] > 0:
				end[n - 1] -= 1
				end[n] += 1
			elif counter[n + 1] and counter[n + 2]:
				end[n + 2] += 1
				counter[n + 1] -= 1
				counter[n + 2] -= 1
			else: return False
		return True 
				
								
a = Solution()
nums = [1,2,3,3,4,5]
#nums = [1,2,3,3,4,4,5,5]
#nums = [1,2,3,4,4,5]
print(a.isPossible(nums))
				

from typing import List
import collections

class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		sums = collections.defaultdict(int)
		
		sums[nums[0]] += 1
		sums[-nums[0]] += 1
		
		for i in range(1, len(nums)):
			
			tmp = collections.defaultdict(int)
			for num in sums:
				tmp[num - nums[i]] += sums[num]   
				tmp[num + nums[i]] += sums[num]
			
			sums = tmp
			
		return sums[target] if target in sums else 0
		
a = Solution()
nums = [1,1,1,1,1]; target = 3
#nums = [1]; target = 1
#nums = [0,0,0,0,0,0,0,0,1]; target = 1
print(a.findTargetSumWays(nums, target))

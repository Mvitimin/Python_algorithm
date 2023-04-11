from typing import List
import collections
class Solution:
	def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
		n, t = len(nums), sum(nums)
		if t % k: return False
		buckets = [t // k] * k
		nums.sort(reverse=True)
		
		def solve(index):
			if index >= n:
				return True
			for i in range(k):
				if buckets[i] >= nums[index]:
					buckets[i] -= nums[index]
					if solve(index + 1): return True
					buckets[i] += nums[index]
			return False
		return solve(0)
		
		
a = Solution()
#nums = [4,3,2,3,5,2,1]; k = 4
#nums = [1,2,3,4]; k = 3
#nums = [1,1,1,1,9]; k = 2
nums = [1,2,3,4]; k = 3
print(a.canPartitionKSubsets(nums, k))

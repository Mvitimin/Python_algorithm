from typing import List
class Solution:
	def smallestDistancePair(self, nums: List[int], k: int) -> int:
		n = len(nums)
		nums.sort()
		def isPossible(guess):
			count = left = 0
			for right in range(1, n):
				while right > left and nums[right] - nums[left] > guess:
					left += 1
				count += (right - left)
			return count >= k
			
		l, r = 0, nums[-1]
		while l < r:
			mid = l + (r - l) // 2
			if isPossible(mid): r = mid 
			else: l = mid + 1
		return l

a = Solution()
nums = [1,3,1]; k = 1
nums = [1,1,1]; k = 2
nums = [1,6,1]; k = 3
#nums = [9,10,7,10,6,1,5,4,9,8]; k = 18
print(a.smallestDistancePair(nums, k))

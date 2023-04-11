from typing import List

class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		nums.sort()
		n = len(nums)
		val = ans = float('inf')
		for k, num in enumerate(nums):
			i, j = k + 1, n - 1
			while i < j:
				s = (num + nums[i] + nums[j])				
				if val > abs(s - target):
					ans, val = s, abs(s - target)
				if target > s: 
					i += 1
				elif target < s:
					j -= 1
				else: 
					return s
		return ans

a = Solution()
nums = [-1,2,1,-4]; target = 1
nums = [0,0,0]; target = 1
print(a.threeSumClosest(nums, target))

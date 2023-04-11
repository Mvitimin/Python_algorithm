from typing import List

class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		n = len(nums)
		if n * k == 0:
			return []
		if len(nums) == 1:
			return nums		
		left = [0] * n
		right = [0] * n
		left[0], right[n - 1] = nums[0], nums[n - 1]
		for i in range(1, n):
			if i % k == 0:
				left[i] = nums[i]
			else:
				left[i] = max(left[i - 1], nums[i])			
			j = n - i - 1
			if (j + 1) % k ==0:
				right[j] = nums[j]
			else:
				right[j] = max(right[j + 1], nums[j])	
		
		ans = []
		for i in range(0, (n - k + 1)):
			ans.append(max(right[i], left[i + k - 1]))	
		return ans
		
nums = [1,3,-1,-3,5,3,6,7]
k = 3		
a = Solution()
print(a.maxSlidingWindow(nums, k))

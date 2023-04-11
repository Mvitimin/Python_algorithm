from typing import List
import bisect
class Solution:
	def nextPermutation(self, nums: List[int]) -> None:	
		n = len(nums)
		idx = -1
		for i in range(n - 2, -1, -1):
			if nums[i] < nums[i + 1]:
				idx = i
				break
		
		l, r = idx + 1, n - 1
		while l <= r:
			nums[l], nums[r] = nums[r], nums[l]
			l += 1
			r -= 1
				
		if idx != -1:
			k = bisect.bisect_right(nums, nums[idx], idx + 1, n - 1)
			nums[k], nums[idx] = nums[idx], nums[k]
		#print(nums)
								
a = Solution()
nums = [1, 2, 3]
#nums = [3, 2, 1]
#nums = [1, 1, 5]
#nums = [1, 3, 10, 9, 2]
#nums = [2,3, 1]
nums = [4,2,0,2,3,2,0]
#nums = [3, 2, 1]
print(a.nextPermutation(nums))


from typing import List

class Solution:
	def splitArray(self, nums: List[int], m: int) -> int:
		n = len(nums)
		l, r = max(nums), sum(nums)
		
		while l <= r:
			mid = l + (r - l) // 2
			pre_sum = cnt = 0
			for i in range(n):
				if pre_sum + nums[i] > mid:
					pre_sum, cnt = nums[i], cnt + 1
				else:
					pre_sum += nums[i]
			if cnt >= m:
				l = mid + 1
			else:
				r = mid - 1	
		return l
					
nums = [7,2,5,10,8]; m = 2	
#nums = [1,2,3,4,5]; m = 2
#nums = [1,4,4]; m = 3
a = Solution()
print(a.splitArray(nums, m))


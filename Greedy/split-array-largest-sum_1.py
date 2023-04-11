from typing import List

class Solution:
	def splitArray(self, nums: List[int], m: int) -> int:
		l, r = max(nums), sum(nums)
		while l <= r:
			mid = l + (r - l) // 2; 
			water = cnt = 0
			for i in nums:
				water += i 
				if water > mid:
					water = i 
					cnt += 1
			if cnt + 1 > m:
				l = mid + 1
			else:
				r = mid - 1
		return l
		
a = Solution()
nums = [7,2,5,10,8]; m = 2
nums = [1,2,3,4,5]; m = 2
nums = [1,4,4]; m = 3
print(a.splitArray(nums, m))

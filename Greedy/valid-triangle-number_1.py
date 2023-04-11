from typing import List

class Solution:
	def triangleNumber(self, nums: List[int]) -> int:
		n = len(nums)
		nums.sort()
		
		ans = 0
		for k in range(n - 1, 1, -1):
			i,j = 0, k - 1
			while i < j:
				if nums[j] + nums[i] > nums[k]:
					ans += (j - i)
					j -= 1
				else:
					i += 1		
		return ans
		
		
a = Solution()
nums = [2, 2, 3, 4]
nums = [4, 2, 3, 4]
#nums = [1, 1, 3, 4]
print(a.triangleNumber(nums))

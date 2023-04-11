from typing import List
class Solution:
		
	def triangleNumber(self, nums: List[int]) -> int:
		nums.sort()
		n = len(nums)
		ans = 0
		for right in range(n - 1, 1, -1):
			i, j = 0, right - 1
			while i < j:
				if nums[i] + nums[j] > nums[right]:
					ans += (j - i)
					j -= 1
				else: i += 1
		return ans

a = Solution()
nums = [2,2,3,4]
nums = [4,2,3,4]
print(a.triangleNumber(nums))					



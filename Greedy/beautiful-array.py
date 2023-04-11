from typing import List

class Solution:
	def beautifulArray(self, n: int) -> List[int]:
		nums = list(range(1, n + 1))
		
		def helper(nums):
			if len(nums) < 3:
				return nums
			even = nums[::2]
			odd = nums[1::2]
			return helper(even) + helper(odd)
		return helper(nums)		
a = Solution()
n = 6
#n = 1
def check(arr):
	for i in range(n - 1):
		seen = set()
		for j in range(i + 1, n):
			val = (arr[i] + arr[j]) / 2
			if val in seen:
				return False
			seen.add(arr[j])
	return True
			

arr = a.beautifulArray(n)
print(arr)
print(check(arr))						
						
								

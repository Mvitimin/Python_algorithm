from typing import List
class Solution:
	def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
		n = len(nums)
		ans = ones = 0
		dp = {0: 1}
		prefix_sum = {0: 1}
		MODULO = 10 ** 9 + 7
		for i, num in enumerate(nums):
			if num == 1:
				ones += 1
			else:
				ones -= 1
			
			dp[ones] = dp.get(ones, 0) + 1
	
			prefix_sum[ones] = prefix_sum.get(ones - 1, 0) + dp.get(ones, 0)
			
			ans += prefix_sum.get(ones - 1, 0) 
		
		return ans % MODULO
		
		
			
							
			

a = Solution()
nums = [0, 1, 1, 0, 1]
nums = [1, 1, 1, 1, 1]
#nums = [0]
print(a.subarraysWithMoreZerosThanOnes(nums))


from typing import List
class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		dp = [float('inf')] * 2
		for n in nums:
			if dp[0] >= n:
				dp[0] = n
			elif dp[1] >= n:
				dp[1] = n
			else:
				return True
		return False

a = Solution()
nums = [1,2,3,4,5]
#nums = [5,4,3,2,1]
#nums = [2,1,5,0,4,6]
print(a.increasingTriplet(nums))		
		
		


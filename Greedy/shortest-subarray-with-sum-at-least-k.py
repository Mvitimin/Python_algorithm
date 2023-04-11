from typing import List
import collections
class Solution:
	def shortestSubarray(self, nums: List[int], k: int) -> int:
		n = len(nums)
		q = collections.deque([-1])
		dp = [0] * (n + 1)
		ans = float('inf')
		
		for i, num in enumerate(nums):
			dp[i] = dp[i - 1] + num
			
			while q and dp[q[-1]] >= dp[i]:
				q.pop()
			
			while q and dp[i] - dp[q[0]] >= k:
				ans = min(ans, i - q.popleft())
			
			q.append(i)
			
			
		return -1 if ans == float('inf') else ans	
		
		
					
			
			
a = Solution()
nums = [1]; k = 1
#nums = [1,2]; k = 4
#nums = [2,-1,2]; k = 3
#nums = [48,99,37,4,-31]; k = 140
#nums = [1, -3, -4, 148]; k = 140
print(a.shortestSubarray(nums, k))

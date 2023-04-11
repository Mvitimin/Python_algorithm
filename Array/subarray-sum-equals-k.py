from typing import List
import collections

class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		
		p = 0
		counter = collections.defaultdict(int)
		counter[p] += 1
		ans = 0
		
		for i, num in enumerate(nums):
			p += num 
			ans += counter[p - k] 
			counter[p] += 1  			
		return ans 	
		
a = Solution()
nums = [1,1,1]; k = 2
nums = [1,2,3]; k = 3
nums = [0,0,0]; k = 0
print(a.subarraySum(nums, k))


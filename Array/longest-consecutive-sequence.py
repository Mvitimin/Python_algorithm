from typing import List
import collections
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		seen = set(nums)
		dict = collections.defaultdict(int) 
		ans = 0
		for i, num in enumerate(nums):
			k, cnt = num, 0
			while k in seen:
				seen.remove(k)
				k -= 1
				cnt += 1	
			dict[num] = cnt + dict[k]	
			ans = max(ans, dict[num])
		return ans	

a = Solution()
nums = [100,4,200,1,3,2]
print(a.longestConsecutive(nums))
			


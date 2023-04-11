from typing import List

class Solution:
	def minNumberOperations(self, target: List[int]) -> int:
		ans = prev = 0
		for cur in target:
			if cur > prev:
				ans += cur - prev
			prev = cur
		return ans
		
		
a = Solution()
target = [1,2,3,2,1]
target = [3,1,1,2]
target = [3,1,5,4,2]
print(a.minNumberOperations(target))
			


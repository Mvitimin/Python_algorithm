from typing import List

class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:	
		ans, tmp = [], []
		def solve(num):
			if len(tmp) == k:
				ans.append(tmp[:])
				return
			for i in range(num + 1, n + 1):
				tmp.append(i)	
				solve(i)
				tmp.pop()
		solve(0)
		return ans
		
a = Solution()
print(a.combine(1, 1))

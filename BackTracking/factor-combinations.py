
from typing import List

class Solution:
	def getFactors(self, n: int) -> List[List[int]]:
		
		tmp = []
		ans = []
		
		def solve(n, prev):
				
			for i in range(prev, int(n ** (1/2)) + 1):
				if i != n and n % i == 0:
					tmp.append(i)
					ans.append(tmp + [n // i])
					solve(n // i, i)
					tmp.pop()
	
		solve(n, 2)
		return ans	
				
a = Solution()
print(a.getFactors(12))

k = [1, 2, 3]
p = k + [4]
print(k)

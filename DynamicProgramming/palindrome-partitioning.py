from typing import List
class Solution:
	def partition(self, s: str) -> List[List[str]]:
		n = len(s)		
		ans = []
		def solve(i, res):	
			if i == n:
				ans.append(res[:])
				return 		
			for k in range(i, n):
				t = s[i:k + 1]
				if t == t[::-1]:
					res.append(t)
					solve(k + 1, res)
					res.pop()
		solve(0, [])
		return ans		
	
a = Solution()
s = "aab"
s = "abbaadddda"
print(a.partition(s))		

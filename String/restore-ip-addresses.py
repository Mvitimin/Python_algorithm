from typing import List

class Solution:
	def restoreIpAddresses(self, s: str) -> List[str]:
		
		n = len(s)
		tmp = []
		ans = []
		
		def solve(i):
			if len(tmp) >= 4 or i == n:
				if len(tmp) == 4 and i == n:		
					ans.append('.'.join(tmp))
				return 
					
			end = (i + 1 if s[i] == '0' else i + 3)	
			for j in range(i, min(n, end)):
				k = s[i:j + 1]
				if 0 <= int(k) <= 255:
					tmp.append(k)
					solve(j + 1)
					tmp.pop()
		
		solve(0)	
		return ans	
		
a = Solution()					
s = "25525511135"
s = "0000"
s = "101023"
print(a.restoreIpAddresses(s))


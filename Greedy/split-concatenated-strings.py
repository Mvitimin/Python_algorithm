from typing import List

class Solution:
	def splitLoopedString(self, strs: List[str]) -> str:
		res = []
		for txt in strs:
			a, b = txt, txt[::-1]
			res.append(a if a > b else b)
		
		ans = ''
		for i, txt in enumerate(strs):
			a, b = txt, txt[::-1]
			prev = ''.join(res[:i])
			next = ''.join(res[i + 1:])
			for j in range(len(txt)):
				p, q = a[j:] + next + prev + a[:j], b[j:] + next + prev + b[:j]
				ans = max(ans, p, q)
		return ans

s = Solution()
strs = ["abc","xyz"]
strs = ["abc"]
print(s.splitLoopedString(strs))
			
			


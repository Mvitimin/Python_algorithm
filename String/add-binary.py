class Solution:
	def addBinary(self, a: str, b: str) -> str:
		p1, p2 = len(a) - 1, len(b) - 1
		
		tmp = 0
		res = ''
		while p1 >= 0 or p2 >= 0:
			if p1 >= 0 and p2 >= 0:
				v1, v2 = int(a[p1]), int(b[p2]) 
				res = str(v1 ^ v2 ^ tmp) + res
				tmp = ((v1 | v2) & tmp) | (v1 & v2)
				p1 -= 1; p2 -= 1
			elif p1 >= 0:
				v1 = int(a[p1])
				res = str(v1 ^ tmp) + res
				tmp = v1 & tmp 
				p1 -= 1
			else:
				v2 = int(b[p2])
				res = str(v2 ^ tmp) + res
				tmp = v2 & tmp
				p2 -= 1
		if tmp:
			res = str(tmp) + res
		return res

s = Solution()
a = "11"; b = "1"		
a = "1010"; b = "1011"												
print(s.addBinary(a, b))
			

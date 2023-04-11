class Solution:
	def minimumSwap(self, s1: str, s2: str) -> int:
		n = len(s1)
		xy = yx = 0
		for i in range(n):
			if s1[i] == 'x' and s2[i] == 'y':
				xy += 1
			elif s1[i] == 'y' and s2[i] == 'x':
				yx += 1
		
		if xy % 2 != yx % 2:
			return -1
		return xy // 2 + yx // 2 + xy % 2 + yx % 2
a = Solution()
s1 = "xx"; s2 = "yy"
s1 = "xy"; s2 = "yx"
s1 = "xx"; s2 = "xy"
print(a.minimumSwap(s1, s2))


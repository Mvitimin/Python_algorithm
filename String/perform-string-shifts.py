from typing import List

class Solution:
	def stringShift(self, s: str, shift: List[List[int]]) -> str:
		n = len(s)
		left_shift = 0
		for direction, amount in shift:
			amount = amount % n
			if direction == 0:
				left_shift += amount
			else:
				left_shift -= amount
		
		return s[left_shift: ] + s[:left_shift]
		
a = Solution()
s = "abc"; shift = [[0,1],[1,2]]
s = "abcdefg"; shift = [[1,1],[1,1],[0,2],[1,3]]
s = "abc"; shift = [[1, 3], [0, 3]]
print(a.stringShift(s, shift))
			


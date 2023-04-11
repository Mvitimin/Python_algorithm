
from typing import List

class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		
		d = 1
		for i in range(len(digits) - 1, -1, -1):
			d, m = divmod(digits[i] + d, 10)
			digits[i] = m		
		if d: digits.insert(0, 1)
		return digits
			
a = Solution()
digits = [9, 8, 9]
print(a.plusOne(digits))

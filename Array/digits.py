from typing import List

class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		
		n = len(digits)
		carry = 1 
		
		for i in range(n - 1, -1, -1):
			if carry:
				if digits[i] == 9:
					digits[i] = 0
				else:
					digits[i] += 1
					carry = 0
		
		if carry:
			digits.insert(0, 1)
		return digits
						
			
a = Solution()
digits = [1, 2, 3]
digits = [4, 3, 2, 1]
digits = [8]
print(a.plusOne(digits))

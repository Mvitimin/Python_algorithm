from typing import List
import collections

class Solution:
	def lemonadeChange(self, bills: List[int]) -> bool:
		coins = collections.defaultdict(int)
		for i, bill in enumerate(bills):
			coins[bill] += 1
			if bill == 20:
				if coins[10] > 0 and coins[5] > 0:
					coins[10] -= 1
					coins[5] -= 1
				elif coins[5] >= 3:
					coins[5] -= 3
				else:
					return False
			if bill == 10:
				if coins[5] == 0: return False
				coins[5] -= 1
		return True	
		

a = Solution()
bills = [5,5,5,10,20]
bills = [5,5,10,10,20]
#bills = [5,5,10]
#bills = [10,10]
#bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
print(a.lemonadeChange(bills))

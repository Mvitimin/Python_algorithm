from typing import List
class Solution:
	def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
		jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
		cheese = (4 * cheeseSlices - tomatoSlices) // 2
		if jumbo < 0 or cheese < 0 or (5 * jumbo + 3 * cheese) != tomatoSlices + cheeseSlices: return []
		return [jumbo, cheese]

a = Solution()
tomatoSlices = 16; cheeseSlices = 7
tomatoSlices = 17; cheeseSlices = 4
tomatoSlices = 4; cheeseSlices = 17
print(a.numOfBurgers(tomatoSlices, cheeseSlices))

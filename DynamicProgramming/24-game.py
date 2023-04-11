from typing import List
import itertools
import math
class Solution:
	def judgePoint24(self, cards: List[int]) -> bool:
		if len(cards) == 1:
			return math.isclose(cards[0], 24)
		return any(self.judgePoint24([x] + rest) for a, b, *rest in itertools.permutations(cards) for x in {a + b, a - b, a * b, b and a/b})

	`
a = Solution()
cards = [1,2,1,2]
#cards = [4,1,8,7]
#cards = [1,3, 4, 6]
print(a.judgePoint24(cards))	
			
			
			

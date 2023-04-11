from typing import List
class Solution:
	def numRabbits(self, answers: List[int]) -> int:
		ans, map = 0, {}
		for i, n in enumerate(answers):
			if n not in map:
				map[n] = n 
			else: 
				map[n] -= 1
			if map[n] < 1: 
				ans += (n + 1)
				del map[n]
		for n in map:
			ans += (n + 1)
		return ans	


answers = [1,1,2]
answers = [10,10,10]
a = Solution()
print(a.numRabbits(answers))

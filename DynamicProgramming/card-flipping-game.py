from typing import List
class Solution:
	def flipgame(self, fronts: List[int], backs: List[int]) -> int:
		return min((set(fronts) | set(backs)) - set([fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]]), default=0)
		

a = Solution()
fronts = [1,2,4,4,7]; backs = [1,3,4,1,3]
fronts = [1, 1]; backs = [1, 2]
print(a.flipgame(fronts, backs))

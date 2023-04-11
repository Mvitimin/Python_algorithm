from typing import List
 
class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		
		ans, tmp = [], []
		def solve(start, t):
			if t == target:
				ans.append(tmp[:])
			elif t > target:
				return 
			for i in range(start, len(candidates)):
				tmp.append(candidates[i])
				solve(i, t + candidates[i])
				tmp.pop()
		solve(0, 0)
		return ans

a = Solution()
#candidates = [2,3,6,7]
#target = 7
#candidates = [2,3,5]
#target = 8
candidates = [2]
target = 1
print(a.combinationSum(candidates, target))


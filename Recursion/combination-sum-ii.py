from typing import List

class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		
		n = len(candidates)
		candidates.sort()
		tmp = []
		ans = []
		
		def solve(i, value):
			
			if value == target:
				ans.append(tmp[:])
				return 
			
			for j in range(i, n):
				if j > i and candidates[j] == candidates[j - 1]:
					continue
				if value + candidates[j] <= target:
					tmp.append(candidates[j])
					solve(j + 1, value + candidates[j])
					tmp.pop()
					
		solve(0, 0)						
		return ans

a = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]; target = 8
#candidates = [2,5,2,1,2]; target = 5
print(a.combinationSum2(candidates, target))	


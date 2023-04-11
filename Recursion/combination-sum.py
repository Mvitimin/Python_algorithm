from typing import List

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		
		candidates.sort()
		n = len(candidates)
		res = {}
		ans = []
		def solve(i, target):
			if i == n:
				if target == 0:
					tmp = []
					for key in res:
						tmp.extend([key] * max(res[key], 0))
					ans.append(tmp)		
				return 
			if target < 0:
				return 
			for k in range(0, target // candidates[i] + 1):
				res[candidates[i]] = k
				solve(i + 1, target - candidates[i] * k)
				del res[candidates[i]]
					
		solve(0, target)			
		return ans

a = Solution()
candidates = [2,3,6,7]; target = 7
candidates = [2,3,5]; target = 8
candidates = [2]; target = 1
print(a.combinationSum(candidates, target))

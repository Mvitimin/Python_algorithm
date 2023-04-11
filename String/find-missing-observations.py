from typing import List

class Solution:
	def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
		m = len(rolls)
		sum1 = sum(rolls)
		sum2 = mean * (n + m) - sum1 		
		v, r = sum2 // n, sum2 % n 
		if not (0 < v <= 6): return []
		ans = [v] * n  
		for i in range(n):
			if r == 0: return ans
			changed = min(6, ans[i] + r)	
			r -= (changed - ans[i])	
			ans[i] = changed
		return [] if r else ans


a = Solution()
rolls = [3,2,4,3]; mean = 4; n = 2
rolls = [1,5,6]; mean = 3; n = 4
rolls = [1,2,3,4]; mean = 6; n = 4
rolls = [1]; mean = 3; n = 1
print(a.missingRolls(rolls, mean, n))			
			

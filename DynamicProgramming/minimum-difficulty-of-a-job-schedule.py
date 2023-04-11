from typing import List
from functools import lru_cache

class Solution:
	def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
		n = len(jobDifficulty)
		@lru_cache(None)
		def helper(index, day, max_difficulty):
			if index == n - 1:
				return max_difficulty if day == d else float('inf')
			if day > d:
				return float('inf')
	
			res = min(max_difficulty + helper(index + 1, day + 1, jobDifficulty[index + 1]), helper(index + 1, day, max(max_difficulty, jobDifficulty[index + 1])))
			return res
		ans = helper(0, 1, jobDifficulty[0])
		return ans if ans != float('inf') else -1	
		
a = Solution()
jobDifficulty = [6,5,4,3,2,1]; d = 2
#jobDifficulty = [9,9,9]; d = 4
#jobDifficulty = [1,1,1]; d = 3
#jobDifficulty = [7,1,7,1,7,1]; d = 3
jobDifficulty = [11,111,22,222,33,333,44,444]; d = 6
print(a.minDifficulty(jobDifficulty, d))				
			
		

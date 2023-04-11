from typing import List
class Solution:
	def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
		l = len(original)
		if l // n != m or n * m != l: return []
		ans = [[0] * n for _ in range(m)]	
		for i in range(l):
			row = i // n; col = i % n
			ans[row][col] = original[i]
		return ans 
			
			
a = Solution()
original = [1,2,3,4]; m = 2; n = 2
original = [5,3,8,9,7,9,1,2,2,3,9]; m =1; n =6
#original = [1,2,3]; m = 1; n = 3
#original = [1,2]; m = 1; n = 1
print(a.construct2DArray(original, m, n))
		

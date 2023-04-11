from typing import List
class Solution:
	def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
		n = len(tops)
		ans = float('inf')
		for i in range(1, 7):
			t = b = com = 0 
			for j in range(n):
				if tops[j] == i and bottoms[j] == i:
					com += 1
				elif tops[j] == i:
					t += 1
				elif bottoms[j] == i:
					b += 1
			if t + b + com == n:
				ans = min(ans, t, b)
		return ans if ans != float('inf') else -1		
			
					
tops = [2,1,2,4,2,2]; bottoms = [5,2,6,2,3,2]
tops = [3,5,1,2,3]; bottoms = [3,6,3,3,4]
tops = [1,2,1,1,1,2,2,2]; bottoms = [2,1,2,2,2,2,2,2]
#tops = [1,1,1,1,1,1,1,1]; bottoms = [1,1,1,1,1,1,1,1]
a = Solution()
print(a.minDominoRotations(tops, bottoms))

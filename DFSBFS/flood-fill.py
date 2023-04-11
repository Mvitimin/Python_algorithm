from typing import List

class Solution:
	def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
		
		m, n = len(image), len(image[0])
		if image[sr][sc] == color:
			return image
		C = image[sr][sc]
		image[sr][sc] = color
		
		def dfs(r, c):
			for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
				if 0 <= dr < m and 0 <= dc < n and image[dr][dc] == C:	
					image[dr][dc] = color
					dfs(dr, dc)
					
		dfs(sr, sc)
	
		return image		

a = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]; sr = 1; sc = 1; color = 2
#image = [[0,0,0],[0,0,0]]; sr = 0; sc = 0; color = 0
print(a.floodFill(image, sr, sc, color))				
		
		

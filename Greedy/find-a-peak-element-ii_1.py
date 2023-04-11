from typing import List


class Solution:
	def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
		m, n = len(mat), len(mat[0])
		
		def val(r, c):
			return mat[r][c] if 0 <= r < m and 0 <= c < n else -1
		
		for i in range(m):
			l, r = 0, n - 1
			while l <= r:
				mid = l + (r - l) // 2
				
				left, right, up, down = val(i, mid - 1), val(i, mid + 1), val(i - 1, mid), val(i + 1, mid)
				
				max_val = max(mat[i][mid], left, right, up, down)
				
				if mat[i][mid] == max_val:
					return [i, mid]
				elif left == max_val:
					r = mid - 1
				elif right == max_val:
					l = mid + 1
				else:
					break
		return [0, 0]

a = Solution()
mat = [[1,4],[3,2]]
mat = [[10,20,15],[21,30,14],[7,16,32]]
print(a.findPeakGrid(mat))

		
				
					
					
						
					
					
			

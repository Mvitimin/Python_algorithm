from typing import List

class Solution:
	def minCostII(self, costs: List[List[int]]) -> int:
		n, m = len(costs), len(costs[0])
		cur = []
		first = second = firstIdx = None
		tmp1 = tmp2 = 0
		tmp1Idx = -1
		
		for i in range(n):
			cur = [float('inf')] * (m)
			first, second = tmp1, tmp2 
			tmp1 = tmp2 = float('inf')
			firstIdx, tmp1Idx = tmp1Idx, -1 
			for j in range(m):
				x = first
				if firstIdx == j:
					x = second									
				cur[j] = min(cur[j], x + costs[i][j])
				if tmp1 >= cur[j]:
					tmp1, tmp2 = cur[j], tmp1
					tmp1Idx = j	
				elif tmp2 > cur[j]:
					tmp2 = cur[j]				
		return min(cur)

a = Solution()
costs = [[1,5,3],[2,9,4]]
costs = [[7,19,11,3,7,15,17,5,6,18,1,15,18,11],[13,18,18,8,13,12,11,13,4,8,2,4,5,20],[14,5,18,4,7,6,1,6,11,6,16,6,13,17],[18,17,11,3,12,4,8,6,2,7,10,9,19,3],[4,3,2,14,11,15,18,1,17,1,6,14,14,9],[9,13,15,14,5,1,1,6,11,15,16,12,10,18],[19,2,11,3,13,4,13,7,16,16,20,18,20,8],[8,19,20,9,18,13,17,1,2,4,3,20,15,9],[9,10,11,6,14,20,4,1,5,15,13,10,13,5],[13,11,9,11,9,16,3,19,1,11,6,7,12,13],[14,1,15,14,11,12,7,14,12,11,6,9,5,5]]
#costs = [[1,3],[2,4]]
print(a.minCostII(costs))

from typing import List
class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		ans = [[1]]
		if numRows >= 2:
			ans.append([1, 1])
		for i in range(3, numRows + 1):
			res = [1]
			for j in range(i - 2):
				res.append(ans[-1][j] + ans[-1][j + 1])
			res.append(1)
			ans.append(res)
		return ans	

a = Solution()	
numRows = 5
print(a.generate(numRows))		
			

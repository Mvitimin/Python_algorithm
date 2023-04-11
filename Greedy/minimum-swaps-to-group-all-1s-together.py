from typing import List

class Solution:
	def minSwaps(self, data: List[int]) -> int:
		k = sum([num for num in data if num == 1])
		if k == 0:
			return 0
		start = zeros = 0
		ans = float('inf')
		for i, num in enumerate(data):
			zeros += (num ^ 1)
			if i - start + 1 == k:
				ans = min(ans, zeros)
				zeros -= (data[start] ^ 1)
				start += 1	
		return ans 
		
a = Solution()
data = [1, 0, 1, 0, 1]
#data = [0, 0 , 0, 1, 0]
data = [1,0,1,0,1,0,0,1,1,0,1]
#data = [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
#data = [0, 1, 1, 0, 1, 0, 1, 1, 0]
data =[1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
#data = [0, 0 , 0]
print(a.minSwaps(data))
			

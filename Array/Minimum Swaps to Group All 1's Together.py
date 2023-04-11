from typing import List

class Solution:
	def minSwaps(self, data: List[int]) -> int:
		n = len(data)
		ones = sum(data)
		start = cnt = 0	
		ans = float('inf')
		for i in range(n):											
			cnt += data[i]
			if i - start + 1 > ones:
				cnt -= data[start]
				start += 1
				
			ans = min(ans, ones - cnt)	
				
		return ans

a = Solution()
data = [1,0,1,0,1,0,0,1,1,0,1]
#data = [1,0,1,0,1]
#data = [0,0,0,1,0]
#data = [1,0,0,1,1,1]
data = [1,0,1,0,1,0,0,1,1,0,1]
print(a.minSwaps(data))		


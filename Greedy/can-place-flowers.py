from typing import List

class Solution:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		m = len(flowerbed)
		for i in range(m):
			if n == 0:
				return True
			left, right = i - 1, i + 1
			if flowerbed[i] == 0:
				if not ((0 <= left and flowerbed[left] == 1) or (right < m and flowerbed[right] == 1)):
					flowerbed[i] = 1
					n -= 1
		return n == 0 

a = Solution()
flowerbed = [1,0,0,0,1]; n = 1
#flowerbed = [0]; n = 1
#flowerbed = [1,0,0,0,1]; n = 2
flowerbed = [1,0,0,0,0,1]; n = 2
print(a.canPlaceFlowers(flowerbed, n))
				
				
						
				
			
			
			

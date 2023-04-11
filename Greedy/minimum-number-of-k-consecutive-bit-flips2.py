from typing import List

class Solution:
	def minKBitFlips(self, A: List[int], K: int) -> int:
		flip, ans, N = 0, 0, len(A)
		spot = [0] * N
		for i, x in enumerate(A):
			flip ^= spot[i]
			if x ^ flip == 0:
				if i + K > N:
					return - 1
				ans += 1
				flip ^= 1
				if i + K < N: spot[i + K] ^= 1
		return ans		
				
		
		
		
a = Solution()


A = [0,0,0,1,0,1,1,0]
K = 3


'''
A = [1,1,0]
K = 2		
'''

'''
A = [0, 1, 1]
K = 2
'''
print(a.minKBitFlips(A, K))		

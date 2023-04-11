from typing import List

class Solution:
	def minKBitFlips(self, A: List[int], K: int) -> int:
		i, ans, v, k = 0, 0, 0, K
		while i < len(A):
			print(i, v)
			if A[i] == v:
				if i + k <= len(A):
					j = i
					ans += 1				
					while j < i + k:
						if A[j] != v:
							v = int(not v)
							 break							
						j += 1
					i = j 
				else:
					return -1
			else:
				i += 1
		
		return ans
		
a = Solution()

'''
A = [0,0,0,1,0,1,1,0] 1
K = 3


A = [1,1,0]
K = 2		
'''

A = [0, 1, 1]
K = 2

print(a.minKBitFlips(A, K))		

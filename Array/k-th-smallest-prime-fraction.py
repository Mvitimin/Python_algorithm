from typing import List
import bisect

class Solution(object):
	def kthSmallestPrimeFraction(self, primes, K):
		l, r = 0, 1
		n = len(primes)
		while True:
			m = (l + r) / 2
			
			res = [bisect.bisect(primes, primes[i] / m) for i in range(n)]
		
			cnt = sum(n - i for i in res)
			if cnt > K:
				r = m 
			elif cnt < K:
				l = m
			else:
				return max([(primes[i], primes[j]) for i, j in enumerate(res) if j < n], key=lambda x : x[0] / x[1])
a = Solution()
arr = [1, 2, 3, 5]; k = 3
arr = [1, 7]; k = 1
print(a.kthSmallestPrimeFraction(arr, k))

				 
			

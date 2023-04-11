import heapq
class Solution:
	def nthUglyNumber(self, n: int) -> int:
		if n == 1:
			return 1
			
		ugly_prime = [2, 3, 5]
		heap = [(1, )]
		
		for i in range(n):
			x, idx = heapq.heappop(heap)
			print(x)
			ans = x
			for j in range(idx, len(ugly_prime)):
				heapq.heappush(heap, (x * ugly_prime[j], j))
	
		return ans	
		
a = Solution()
n = 1690
#n = 10
n = 10
print(a.nthUglyNumber(n))

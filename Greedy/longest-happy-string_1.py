import heapq

class Solution:
	def longestDiverseString(self, a: int, b: int, c: int) -> str:
		heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
		heap.sort()
		while heap and heap[-1][0] == 0:
			heap.pop()	
		ans = ''
		while heap:
			n, c = heapq.heappop(heap)
			if len(ans) > 1 and ans[-1] == ans[-2] == c:
				tn, tc = n, c
				if not heap: break
				n, c = heapq.heappop(heap)
				heapq.heappush(heap, (tn, tc))
			ans += c
			n += 1
			if n < 0:
				heapq.heappush(heap, (n, c))
		return ans

s = Solution()
a = 1; b = 1; c = 7
a = 7; b = 1; c = 0
print(s.longestDiverseString(a, b, c))
		

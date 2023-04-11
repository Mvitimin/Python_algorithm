from collections import Counter
import heapq

class Solution:
	def minDeletions(self, s: str) -> int:
		heap = []
		counter = Counter(s)
		seen = set()
		for c in counter:
			if counter[c] in seen:
				heapq.heappush(heap, (-counter[c], c))
			else:
				seen.add(counter[c])
		ans = 0
		while heap:
			num, c = heapq.heappop(heap)
			num *= -1
			for i in range(num - 1, -1, -1):
				if i == 0:
					ans += num 
					break
				elif i not in seen:
					ans += (num - i)
					seen.add(i)
					break
		return ans
		
a = Solution()
#s = "aaabbbccc"
s = "bbcebab"
print(a.minDeletions(s))

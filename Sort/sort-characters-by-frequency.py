import collections

class Solution:
	def frequencySort(self, s: str) -> str:
		counter = collections.Counter(s)	
		keys = list(counter.keys())
		keys.sort(key=lambda x : -counter[x])			
		ans = []
		for chr in keys:
			ans.append(chr * counter[chr])			
		
		return ''.join(ans)

a = Solution()
s = "tree"
s = "cccaaa"
s = "Aabb"
s = "loveleetcode"
print(a.frequencySort(s))			
		
		
			
			

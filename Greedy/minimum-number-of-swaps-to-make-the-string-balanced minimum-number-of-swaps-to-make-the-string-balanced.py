class Solution:
	def minSwaps(self, s: str) -> int:
		ans = neg = 0
		for c in s:
			if c == ']':
				neg -= 1
			else: neg += 1
			ans = min(neg, ans)
		return (-ans + 1) // 2	
			
a = Solution()
s = "][]["
#s = "]]][[["
#s = "[]"
print(a.minSwaps(s))
			

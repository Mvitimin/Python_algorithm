class Solution:
	def countVowelPermutation(self, n: int) -> int:	
		prev = [1] * 5	
		for i in range(1, n):
			cur = [0] * 5
			cur[0] = prev[1] + prev[2] + prev[4] # ea, ia, ua
			cur[1] = prev[0] + prev[2] # ae, ie
			cur[2] = prev[1] + prev[3] # ei, oi 
			cur[3] = prev[2] # io
			cur[4] = prev[2] + prev[3] # iu, ou
			prev = cur
		
		return sum(prev) % (10 ** 9 + 7)
		
a = Solution()
print(a.countVowelPermutation(5))		

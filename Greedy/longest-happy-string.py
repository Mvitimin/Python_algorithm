class Solution:			
	def longestDiverseString(self, a: int, b: int, c: int) -> str:
		arr = ['a' * a, 'b' * b, 'c' * c]
		arr.sort(key=lambda x:len(x))
		init = list([arr[-1][i:i + 2] for i in range(0, len(arr[-1]), 2)])	
		i, j, k = 0, len(arr[0]) - 1, len(arr[1]) - 1
		interval = min(len(init) - 1, len(arr[0]) + len(arr[1]))
		while j >= 0 or k >= 0:
			if j >= 0:
				init[i] += arr[0][j]
				j -= 1
			else:
				init[i] += arr[1][k]
				k -= 1
			i = (i + 1) % len(init)		
		return ''.join(init[:interval + 1])
		
											
s = Solution()
#a = 3; b = 3; c = 5;
#a = 4; b = 4; c = 2;
#a = 7; b = 1; c = 0
#a = 8; b = 2; c = 1
a = 3; b = 3; c = 1
a = 1; b = 1; c = 7
a = 7; b = 1; c = 0
print(s.longestDiverseString(a, b, c))

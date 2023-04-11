class Solution:
	def monotoneIncreasingDigits(self, n: int) -> int:
		while n:
			arr = list(str(n))
			m = len(arr)
			for i in range(1, m):
				if arr[i - 1] > arr[i]:
					arr[i - 1] = str(int(arr[i - 1]) - 1)
					n = int(''.join(arr[:i]) + '9' * (m - i))
					break
			else: break
		return n
a = Solution()
n = 1231 
#n = 1234
#n = 1101
n = 3330
#n = 332
print(a.monotoneIncreasingDigits(n))

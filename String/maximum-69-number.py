class Solution:
	def maximum69Number (self, num: int) -> int:
		k = num
		x = 0
		ans = -1
		while k:
			d, m = divmod(k, 10)
			if m == 6:
				ans = x
			x += 1
			k = d
			
		return num + (10 ** ans) * 3	if ans != -1 else num

a = Solution()
num = 9669
num = 9996
num = 9999
print(a.maximum69Number(num))

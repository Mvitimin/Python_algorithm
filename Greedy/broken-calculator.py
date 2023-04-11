class Solution:
	def brokenCalc(self, startValue: int, target: int) -> int:
		x = 0
		while target > startValue:
			if target % 2 == 0:
				target = target // 2 
			else: 
				target += 1
			x += 1
		return x + (startValue - target)
																										
a = Solution()
startValue = 3; target = 10 #3
#startValue = 14; target = 17 #7
#startValue = 2; target = 9 #6
#startValue = 3; target = 10 #3
#startValue = 5; target = 8 #2
#startValue = 2; target = 3 #2
ans = a.brokenCalc(startValue, target)
print(ans)

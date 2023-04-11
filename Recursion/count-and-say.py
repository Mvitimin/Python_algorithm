class Solution:
	def countAndSay(self, n: int) -> str:
		ans = '1'
		txt, cnt, ch = '', 0, ans[0]
		for i in range(2, n + 1):	
			for j, c in enumerate(ans):
				if j == 0:
					cnt, ch = 1, ans[0] 
				elif c != ans[j - 1]:
					txt += (str(cnt) + ch)
					cnt, ch = 1, c
				else: 
					cnt += 1
			ans = txt + (str(cnt) + ch)
			txt = ''	
		return ans

a = Solution()
n = 30
print(a.countAndSay(n))

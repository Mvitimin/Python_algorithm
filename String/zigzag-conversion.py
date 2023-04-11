class Solution:
	def convert(self, s: str, numRows: int) -> str:
		table = [[] for _ in range(numRows)]
		
		row, exp = -1, 1
		for i in range(len(s)):
			row += exp
			row = max(row, 0)
			table[row].append(s[i])
			if row == numRows - 1:
				exp = -1
			elif row == 0:
				exp = 1
			
		ans = []
		for i in range(numRows):
			ans.append(''.join(table[i]))
		return ''.join(ans)

a = Solution()
s = "PAYPALISHIRING"; numRows = 3
s = "PAYPALISHIRING"; numRows = 4
s = "A"; numRows = 1
s = "ABC"; numRows = 1
print(a.convert(s, numRows))0

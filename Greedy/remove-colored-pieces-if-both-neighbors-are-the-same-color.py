class Solution:
	def winnerOfGame(self, colors: str) -> bool:
		i = 0
		n = len(colors)
		counts = {'A': 0, 'B': 0}
		for j, c in enumerate(colors):
			if j == n - 1 or colors[i] != colors[j + 1]:
				counts[colors[i]] += max(0, j - i - 1)
				i = j + 1
		return counts['A'] > counts['B']	
	
a = Solution()
colors = "AAABABB"
colors = "AA"
colors = "ABBBBBBBAAA"
colors = "AAAABBBB"
print(a.winnerOfGame(colors))

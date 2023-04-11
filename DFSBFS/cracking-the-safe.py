from itertools import product

class Solution:
	def crackSafe(self, n: int, k: int) -> str:
		digits, graph, ans = range(k), {}, []
		nodes = list(product(digits, repeat = n - 1))
		for node in nodes:
			graph[node] = list(range(k))
		
		node = tuple([0] * (n - 1))
		ans.extend(node)
		while node in graph and graph[node]:
			edge = graph[node].pop()
			ans.append(edge)
			node = (node + (edge, ))[1:]
			print(node)
		return ''.join(map(str, ans))

a = Solution()
n = 1; k = 2
n = 3; k = 3
print(a.crackSafe(n, k))


#print(*product('1234', repeat = 2))

import collections

def journeyToMoon(n, astronaut):
	
	graph = collections.defaultdict(list)
	
	for u, v in astronaut:
		graph[u].append(v)
		graph[v].append(u)
	
	visited = set()	
	def bfs(u):
		visited.add(u)
		k = 1
		q = collections.deque([u])
		while q:
			u = q.popleft()			
			for v in graph[u]:
				if v not in visited:
					visited.add(v)
					k += 1
					q.append(v)
		return k
	
	p = []
	for i in range(n):
		if i not in visited:
			p.append(bfs(i))
	
	total = sum(p)
	ans = 0
	for i in p:
		total -= i
		ans += total * i 
	return ans

n = 5; astronaut = [[0, 1], [2, 3], [0, 4]]
n = 6; astronaut = [[0, 1], [2, 3]]
res = journeyToMoon(n, astronaut)		
print(res)
			
			
		
			
	
	

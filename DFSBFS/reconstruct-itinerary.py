from typing import List
import collections
class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		
		graph = collections.defaultdict(list)
		for start, end in sorted(tickets, reverse=True):
			graph[start].append(end)
		
		ans = []
		def dfs(node):
			
			while	graph[node]:
				dfs(graph[node].pop())
			ans.append(node)
		
		dfs('JFK')
		return ans[::-1]
		
a = Solution()
#tickets =  [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets =  [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
#tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
#tickets = [["JFK", "ATL"], ["JFK", "SFO"], ["SFO", "JFK"]]
#tickets = [["JFK", "ATL"], ["ATL", "JFK"], ["JFK", "SFO"]]
print(a.findItinerary(tickets))

from typing import List
import collections

class Solution:
	def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
		
		wordSet = set(wordList)
		if endWord not in wordSet: return 0
		
		alphabet = [chr(i + 97) for i in range(26)]
		graph = collections.defaultdict(list)
		wordList.append(beginWord)
														
		for w in wordList:
			for i in range(len(w)):
				for c in alphabet:
					txt = w[:i] + c + w[i + 1:]
					if txt in wordSet:
						graph[w].append(txt)
		
		q = collections.deque([(1, beginWord)])
		visited = set()
		
		while q:
			cnt, u = q.popleft()
			if u == endWord: return cnt
			visited.add(u)			
			for v in graph[u]:
				if v not in visited:
					q.append((cnt + 1, v))										
		return 0				
				
				
a = Solution()
beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"; endWord = "cog"; wordList = ["hot","dot","dog","lot","log"]
print(a.ladderLength(beginWord, endWord, wordList))

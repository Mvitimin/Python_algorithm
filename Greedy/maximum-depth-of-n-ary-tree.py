class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children

class Solution:
	def maxDepth(self, root: 'Node') -> int:
		if not root:
			return 0 
		if not root.children:
			return 1		
		return max(1 + self.maxDepth(node) for node in root.children)

a = Solution()
node1 = Node(3)
node1.children = [Node(5), Node(6)]
root = Node(1)
root.children = [node1, Node(2), Node(4)]
print(a.maxDepth(root))

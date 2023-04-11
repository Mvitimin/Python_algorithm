class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def insertionSortList(self, head: ListNode) -> ListNode:
		if not head:
			return head
		root, node = ListNode(), head
		while node:
			p = root
			while p.next and p.next.val < node.val:
				p = p.next
			p.next, node.next, next = node, p.next, node.next
			
			node = next
		return root.next
				 
			

def printNode(node):
	while node:
		print(node.val, end='->')
		node = node.next
	print()
a = Solution()
node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)
root = a.insertionSortList(node)
printNode(root)

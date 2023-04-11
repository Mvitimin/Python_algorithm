class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def insertionSortList(self, head: ListNode) -> ListNode:
		if not head:
			return head
		root = node = ListNode()
		while head:
			while node.next and node.next.val < head.val:
				node = node.next	
				
			node.next, head.next, head = head, node.next, head.next
			
			if head and node.val > head.val:
				node = root
			
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

"""
My answer:
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head!=None:
            node = head
            while node.next:
                if node.next.val == node.val: 
                    empty = node.next              
                    node.next = node.next.next
                    empty = None              #清除野指针 
                else:
                    node = node.next
        return head
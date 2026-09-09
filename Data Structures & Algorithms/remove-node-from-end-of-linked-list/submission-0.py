# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        back = dummy
        front = dummy
        i = 1
        while i<=n:
            front = front.next
            i+=1
        while front.next is not None:
            back = back.next
            front = front.next
        back.next = back.next.next
        return dummy.next
        
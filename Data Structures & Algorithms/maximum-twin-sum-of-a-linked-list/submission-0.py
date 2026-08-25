# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        nextt = None
        while curr:
            nextt = curr.next
            curr.next = prev

            prev = curr
            curr = nextt
        hd1, hd2 = head, prev
        max_sum = 0
        while hd2:
            max_sum = max(max_sum, hd1.val+hd2.val)
            hd1 = hd1.next
            hd2 = hd2.next
        return max_sum
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        pointer1 = list1
        pointer2 = list2
        while pointer1 is not None and pointer2 is not None:
            if pointer1.val < pointer2.val:
                tail.next = pointer1
                pointer1= pointer1.next
            else:
                tail.next = pointer2
                pointer2 = pointer2.next
            tail = tail.next

        if pointer1 is not None:
            tail.next = pointer1
        else:
            tail.next = pointer2

        return dummy.next
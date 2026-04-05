# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast = head
        # slow = head
        # while fast and fast.next :
        #     fast = fast.next.next # i am trying to access next.next if next is None than everything breaks
        #     slow = slow.next

        #     if slow == fast:
        #         return True

        # return False

        slow = fast = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


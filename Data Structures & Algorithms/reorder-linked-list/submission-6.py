# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # we first need a pointer to the middle node for this we create a fast and slow pointer

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #once we got the middle pointer, we now reverse the linklist

        # naming it second because we would be merging it with the first linklist.
        prev = None
        second = slow.next
        slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1


            first = tmp1
            second = tmp2

        




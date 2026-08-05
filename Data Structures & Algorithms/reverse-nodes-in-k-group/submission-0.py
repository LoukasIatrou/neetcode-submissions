# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pointer = head
        for _ in range(k):
            if pointer is None:
                return head 
            pointer = pointer.next
        prev, curr = pointer , head 
        count = 1
        while count <= k:
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 
            count += 1
        head.next = self.reverseKGroup(pointer,k)
        return prev 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # I need to keep track of the previus node as well as the current. Then i can keep a current count when I iterate through the list once and another count when i do count - n.
        curr = head 
        count = 0
        while curr:
            count +=1 
            curr = curr.next 
        need = count - n
        if need == 0:
            return head.next
        curr = head 
        for i in range(count-1):
            if (i+1) == need:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head



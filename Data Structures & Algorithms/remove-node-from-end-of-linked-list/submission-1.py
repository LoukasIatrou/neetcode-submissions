# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # I need to keep track of the previus node as well as the current. Then i can keep a current count when I iterate through the list once and another count when i do count - n.
        p = head 
        count = 0
        while p:
            count +=1 
            p = p.next 
        need = count - n
        dummy = ListNode(0,head)
        prev = dummy 
        curr = head 
        while need != 0:
            prev = curr 
            curr = curr.next 
            need -= 1
        
        prev.next = curr.next 
        
        return dummy.next



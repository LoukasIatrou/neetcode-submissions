# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#When merging 2 sorted linkedlists we go through each node in the beginning of the list and compare them amongst the others. However now i am left with k lists which makes this way harder, unless i recursively link 2 lists using this approach
        k = len(lists)
        def merge(l1,l2):
            dummy = ListNode()
            tail = dummy 
            while l1 and l2:
                if l1.val<l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next 
            tail.next = l1 or l2 
            return dummy.next
        while len(lists)>1:
            merged = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 <len(lists) else None
                merged.append(merge(l1,l2))
            lists = merged
        return lists[0] if lists else None







# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head 
        seen = set()
        while curr:
            if curr in seen: 
                return True
            seen.add(curr)
            curr = curr.next
        return False
    
    # time : o(n) looping through the entire linked list 
    # space this is also gonne be O(n) time because we maintain a hashset.

    ########################################################## SMARTER SOLUTION ##########################################################

    class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast= head, head 
        while fast and fast.next: 
            slow= slow.next
            fast = fast.next.next 
            if slow == fast : 
                return True
        return False
    
    # this time complexity is O(n) but O(1) space because we are not using any extra data structure. 

    # the intuition here is that if there is a cycle the fast pointer will eventually meet and lap the slow pointer 
    # if they are equal than a cycle exists.
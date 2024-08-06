class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to form the base of the new list
        dummy = ListNode()
        # Set a pointer to the current position in the new list
        current = dummy
        
        # Traverse both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # At this point, one of the lists is exhausted. Append the other list to the result
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Return the merged list, which starts at dummy.next
        return dummy.next
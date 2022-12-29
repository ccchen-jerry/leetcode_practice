# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None:
            odd_node = odd_head = head
            head = head.next
        else:
            return None
        if head is not None:
            even_node = even_head = head
            head = head.next
        else:
            return odd_head
        count = 3
        while head is not None:
            if count % 2 == 1:
                odd_node.next = head
                odd_node = odd_node.next
            else:
                even_node.next = head
                even_node = even_node.next
            head = head.next
            count = count + 1
        odd_node.next = even_head
        even_node.next = None
        return odd_head  
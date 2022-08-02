from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head

class Solution:
    def insert_stack(self, head):
        stack_values = []
        while head:
            stack_values.append(head.val)
            head = head.next
        return stack_values

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack_values = self.insert_stack(head)
        mid = (len(stack_values) // 2) + 1

        count = 1
        mid_node = head
        while count < mid:
            mid_node = mid_node.next
            count += 1

        return mid_node

if __name__ == '__main__':
    head = make_list([1, 2, 3, 4, 5, 6])

    solution = Solution()
    mid_node = solution.middleNode(head)
    print(mid_node.val)
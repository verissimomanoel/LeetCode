from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert_stack(self, head):
        stack_rev = []
        while head:
            stack_rev.append(head.val)
            head = head.next
        return stack_rev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        stack_rev = self.insert_stack(head)

        while head:
            if head.val == stack_rev.pop():
                head = head.next
            else:
                return False
        return True


def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


if __name__ == '__main__':
    head = make_list([1, 2, 2, 1])

    solution = Solution()
    val = solution.isPalindrome(head)
    print(val)
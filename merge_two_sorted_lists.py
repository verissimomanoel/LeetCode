# https://zhenyu0519.github.io/2020/07/10/lc21/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = new_list = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                new_list.next = list1
                list1 = list1.next
            else:
                new_list.next = list2
                list2 = list2.next

            new_list = new_list.next

        new_list.next = list1 or list2

        return head.next


def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


if __name__ == '__main__':
    list1 = make_list([1, 2, 4])
    list2 = make_list([1, 3, 4])

    solution = Solution()
    val = solution.mergeTwoLists(list1, list2)
    print(val)

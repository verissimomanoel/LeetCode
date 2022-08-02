from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbersBest(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        pointer = result

        while (l1 or l2 or carry):
            first_num = l1.val if l1.val else 0
            second_num = l2.val if l2.val else 0

            summation = first_num + second_num + carry

            num = summation % 10
            carry = summation // 10

            pointer.next = ListNode(num)

            pointer = pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = ''
        head = l1
        while head:
            val1 = str(head.val) + val1
            head = head.next

        val2 = ''
        head = l2
        while head:
            val2 = str(head.val) + val2
            head = head.next

        total = int(val1) + int(val2)

        two_sum = []
        pos = 0
        for c in reversed(str(total)):
            two_sum.append(int(c))
            pos += 1

        return make_list(two_sum)


def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


if __name__ == '__main__':
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    head1 = make_list(l1)
    head2 = make_list(l2)

    solution = Solution()
    val = solution.addTwoNumbers(head1, head2)
    print(val)

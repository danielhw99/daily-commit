# ListNode는 LeetCode 실행 환경에서 제공됩니다.
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        answerNode = ListNode()
        current = answerNode
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            carry = sum // 10
            value = sum % 10

            current.next = ListNode(value)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return answerNode.next

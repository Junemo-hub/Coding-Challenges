# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next   # 다음 노드 저장
            current.next = prev        # 방향 뒤집기
            prev = current             # prev 앞으로 이동
            current = next_node        # current 앞으로 이동

        return prev  # prev가 새 head

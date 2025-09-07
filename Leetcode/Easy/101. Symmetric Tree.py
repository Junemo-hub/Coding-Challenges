# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(rl, rr):
            if not rl and not rr:
                return True  # 둘 다 None이면 대칭
            if not rl or not rr:
                return False  # 하나만 None이면 비대칭
            if rl.val != rr.val:
                return False  # 값 다르면 비대칭
            return isMirror(rl.left, rr.right) and isMirror(rl.right, rr.left)

        return isMirror(root.left, root.right)
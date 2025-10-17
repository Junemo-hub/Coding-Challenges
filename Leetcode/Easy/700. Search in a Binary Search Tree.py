# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: root is None or found the value
        if root is None or root.val == val:
            return root
        
        # If value is less than current node's value, go left
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # If value is greater than current node's value, go right
        return self.searchBST(root.right, val)
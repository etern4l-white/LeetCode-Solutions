# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        if target == root.val:
            return root
        if not root.left and not root.right:
            return None
        if root.left and target == root.left.val: return root.left
        elif root.right and target == root.right.val: return root.right
        elif target < root.val:
            return self.searchBST(root.left, target)
        else:
            return self.searchBST(root.right, target)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def track(self, node, l):
        if node == None:
            return l-1
        l1 = self.track(node.left,l+1)
        l2 = self.track(node.right,l+1)
        return max(l1, l2)
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l = 1
        if root == None:
            return 0
        l1 = self.track(root.left, l+1)
        l2 = self.track(root.right, l+1)
        return max(l1, l2)
        

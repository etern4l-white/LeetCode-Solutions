# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def track(self, node, ar):
        if node:
            ar.append(node.val)
            if node.left:
                ar.append(node.left.val)
            if node.right:
                ar.append(node.right.val)
            self.track(node.left, ar)
            self.track(node.right, ar)
        else:
            ar.append(None)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lp = []
        self.track(p,lp)
        lq = []
        self.track(q,lq)
        return lp==lq

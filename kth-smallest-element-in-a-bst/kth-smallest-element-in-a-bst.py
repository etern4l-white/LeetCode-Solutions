# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def track(self, node, nums_list):
        nums_list.append(node.val)
        if node.left:
            self.track(node.left, nums_list)
        if node.right:
            self.track(node.right, nums_list)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = []
        self.track(root, n)
        return sorted(n)[k-1]

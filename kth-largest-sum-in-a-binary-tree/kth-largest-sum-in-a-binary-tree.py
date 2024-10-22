# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def track(self, node, sums, level):
        if level not in sums:
            sums[level] = 0
        sums[level]+=node.val
        if node.left:
            self.track(node.left, sums, level+1)
        if node.right:
            self.track(node.right, sums, level+1)
        
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = {}
        i = 1
        sums[i] = root.val
        if root.left:
            self.track(root.left, sums, i+1)
        if root.right:
            self.track(root.right, sums, i+1)
        values = sorted(sums.values(), reverse=True)
        return values[k-1] if len(values) >=k else -1

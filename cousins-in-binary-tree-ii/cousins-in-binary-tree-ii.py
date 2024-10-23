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

    def track_2(self, node, sums, level):
        if level > 1:
            if level == 2:
                node.val = 0
            if node.right or node.left:
                outer = sums[level+1]
                if node.right:
                    outer-=node.right.val
                if node.left:
                    outer-=node.left.val
                if node.right:
                    node.right.val = outer
                if node.left:
                    node.left.val = outer
        else:
            node.val = 0
        if node.right:
            self.track_2(node.right, sums, level+1)
        if node.left:
            self.track_2(node.left, sums, level+1)
        

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = {}
        sums[1] = root.val
        i = 1
        if root.left:
            self.track(root.left, sums, i+1)
        if root.right:
            self.track(root.right, sums, i+1)
        self.track_2(root, sums, 1)
        return root

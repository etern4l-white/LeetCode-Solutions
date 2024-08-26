"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def track(self, node, ll):
        if node.children != []:
            for child in node.children:
                if child:
                    self.track(child, ll)
            ll.append(node.val)
        else:
            ll.append(node.val)
        
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        else:
            ll = []
            self.track(root, ll)
        
        return ll
        

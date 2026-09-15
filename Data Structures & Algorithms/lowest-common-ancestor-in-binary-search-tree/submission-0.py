# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        curr = root.val
        if curr > p.val and curr>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if curr<p.val and curr<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        return root
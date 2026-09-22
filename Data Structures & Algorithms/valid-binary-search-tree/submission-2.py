# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root)
    def validBST(self, node, mini=float('-inf'), maxi=float('inf')):
        if node is None:
            return True
        if node.val<=mini or node.val>=maxi:
            return False
        left = self.validBST(node.left,mini,node.val)
        right = self.validBST(node.right,node.val,maxi)
        return left and right
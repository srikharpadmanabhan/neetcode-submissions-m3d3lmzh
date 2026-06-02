# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, small, big):

            if not root:
                return True
            
            if small is not None and root.val <= small:
                return False
            
            if big is not None and root.val >= big:
                return False
            
            print(small, big, root)
            return helper(root.left, small, root.val) and helper(root.right, root.val, big)
        
        return helper(root, None, None)
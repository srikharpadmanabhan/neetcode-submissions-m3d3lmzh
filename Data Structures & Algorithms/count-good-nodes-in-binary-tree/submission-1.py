# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(root, max_in_path_so_far):

            if not root:
                return 0
            
            if root.val >= max_in_path_so_far:
                return 1 + helper(root.left, root.val) + helper(root.right, root.val)
            else:
                return helper(root.left, max_in_path_so_far) + helper(root.right, max_in_path_so_far)

            
        
        return helper(root, -101)
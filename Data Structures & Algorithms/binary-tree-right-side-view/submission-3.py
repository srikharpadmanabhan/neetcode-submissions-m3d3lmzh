# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [(0, root)]

        temp = dict()

        levels = 0
        while q:
            idx, top = q.pop(0)
            if idx not in temp:
                temp[idx] = top.val
            
            levels = idx
            if top.right:
                q.append((idx+1, top.right))
            if top.left:
                q.append((idx+1, top.left))

        return [temp[i] for i in range(levels+1)]

            
        


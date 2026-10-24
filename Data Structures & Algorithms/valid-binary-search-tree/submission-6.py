# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, float('-inf'), float('inf')))
        while q:
            n, l, r = q.popleft()
            if n.val <= l or n.val >= r:
                return False
            if n.left:
                q.append((n.left, l, n.val))
            if n.right:
                q.append((n.right, n.val, r))
        return True
                      

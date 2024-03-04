# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _tree_height(self, root):
        """
            this function return the height of the sub tree
            parameters:
                root: the root you will start get the height from it
                height: the height of the subtree
            returns: the height of the sub tree
        """
        # if no root, return -1
        if not root:
            return -1
        
        # return the max of left and right
        return 1 + max(self._tree_height(root.left), self._tree_height(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            this function return the diameter of a binary tree
            returns: the length of the longest path between any two nodes in a tree
        """
        # get left and right height and increase it by 1
        left_height = self._tree_height(root.left) + 1
        right_height = self._tree_height(root.right) + 1
        
        # return the sum of each height
        return left_height + right_height
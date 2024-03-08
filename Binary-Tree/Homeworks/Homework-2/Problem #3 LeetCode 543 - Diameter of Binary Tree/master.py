# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def _tree_height(self, root):
#         """
#             this function return the height of the sub tree
#             parameters:
#                 root: the root you will start get the height from it
#                 height: the height of the subtree
#             returns: the height of the sub tree
#         """
#         # if no root, return -1
#         if not root:
#             return -1
        
#         # return the max of left and right
#         return 1 + max(self._tree_height(root.left), self._tree_height(root.right))
#     def _diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         """
#             this function return the diameter of a binary tree
#             returns: the length of the longest path between any two nodes in a tree
#         """
#         # if no root, return -1
#         if not root:
#             return -1
        
#         # get left and right height and increase it by 1
#         left_height = self._tree_height(root.left) + 1
#         right_height = self._tree_height(root.right) + 1
        
#         # return the sum of each height
#         return left_height + right_height
    
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         """
#             this function return the diameter of a binary tree
#             returns: the length of the longest path between any two nodes in a tree
#         """
#         # if no root, return none
#         if not root:
#             return -1
        
#         # get last left and right node
#         left_node = self.diameterOfBinaryTree(root.left)
#         right_node = self.diameterOfBinaryTree(root.right)
        
        
#         return max(left_node, right_node, self._diameterOfBinaryTree(root))

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
            this function return the diameter of a binary tree
            returns: the length of the longest path between any two nodes in a tree
        """
        # init diameter
        self.diameter = 0
        
        # get long path for the root
        self._long_path(root)
        
        # return diameter
        return self.diameter
    def _long_path(self, current):
        # if no current return 0
        if not current:
            return 0
        
        # get height for the left and right
        left_height = self._long_path(current.left)
        right_height = self._long_path(current.right)
        
        # set the diameter
        self.diameter = max(self.diameter, left_height + right_height)
        
        # return the longest for each current
        
        return 1 + max(left_height, right_height)
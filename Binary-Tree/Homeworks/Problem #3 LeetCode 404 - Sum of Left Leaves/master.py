# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # if not root return 0
        if not root:
            return 0

        # call same function for left and right to arraive to the heighst node
        left_side = self.sumOfLeftLeaves(root.left)
        right_side = self.sumOfLeftLeaves(root.right)

        # sum the values of left and right
        sum_sides = left_side + right_side

        # if the current node has left node, and the left node is leaf add it so the sum_sides

        if root.left and not root.left.left and not root.left.right:
            return sum_sides + root.left.val

        # return the sum
        return sum_sides

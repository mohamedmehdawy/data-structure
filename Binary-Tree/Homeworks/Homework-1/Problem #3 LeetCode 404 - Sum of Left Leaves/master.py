# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionV1:
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
            return root.left.val

        # return the sum
        return sum_sides


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], is_left=False) -> int:
        # if not root return 0
        if not root:
            return 0

        # if the root is leaf
        if not root.left and not root.right:
            # if is left leaf return the root value, else return 0
            return root.val if is_left else 0

        # return the sum of left and right
        return self.sumOfLeftLeaves(root.left, is_left=True) + self.sumOfLeftLeaves(root.right)

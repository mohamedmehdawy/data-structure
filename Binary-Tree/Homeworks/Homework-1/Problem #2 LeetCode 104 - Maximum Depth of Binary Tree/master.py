# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# v1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not elements return 0
        if not root:
            return 0

        def arriveToMaxDepth(current, prev_depth):
            """
                this function walk until arrive to max depth
                parameters:
                    current: the current node will start to get the max of left and right
                    prev_depth: the previous depth of the current node
                return:
                        the max depth of left and right
            """
            # stop case
            if not current:
                return prev_depth

            # init current depth
            current_depth = prev_depth + 1

            # get left max
            left_max = arriveToMaxDepth(current.left, current_depth)

            # get right max
            right_max = arriveToMaxDepth(current.right, current_depth)

            return max(left_max, right_max)

        return arriveToMaxDepth(root, 0)


# v2
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not elements return 0
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

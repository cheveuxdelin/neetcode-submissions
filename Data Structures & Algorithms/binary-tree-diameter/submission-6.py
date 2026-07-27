# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we bubble up the best solution from each subree
# and we simoultanously also return the current best local answer
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # (best_solution, best_local_answer)
        def helper(current):
            if not current:
                return (0, 0)

            left_best_solution, left_longest_path = helper(current.left)
            right_best_solution, right_longest_path = helper(current.right)

            current_best_solution = left_longest_path + right_longest_path

            if current.val == 5:
                print(left_best_solution, left_longest_path)
                print(right_best_solution, right_longest_path)
                print(current_best_solution)

                print(
                    max(
                        left_best_solution,
                        right_best_solution,
                        current_best_solution
                    ),
                    1 + max(left_longest_path, right_longest_path)
                )

            return (
                max(
                    left_best_solution,
                    right_best_solution,
                    current_best_solution
                ),
                1 + max(left_longest_path, right_longest_path)
            )
        return helper(root)[0]
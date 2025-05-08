# time complexity: O(n)
# space complexity: O(1)
# Using stack, save open parentheses and check
# if the last open parentheses is matched with the current close parentheses
class Solution(object):
    def isValid(self, s):
        parenthesesPairs = {"(": ")", "{": "}", "[": "]"}
        close_parentheses = parenthesesPairs.values()

        stack = []

        for char in s:
            if char in parenthesesPairs:
                stack.append(char)
            elif char in close_parentheses:
                if stack and parenthesesPairs[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return True if not stack else False

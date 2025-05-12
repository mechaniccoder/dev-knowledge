from typing import List

# Time complexity: O(n)
# Space complexity: O(n)
# python에서 int()를 호출하면 소숫점을 버린 정수를 리턴하게 된다.
# 소숫점을 버리고 싶을때 잘 활용하자.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 + operand2)
            elif token == '-':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 - operand2)
            elif token == '*':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 * operand2)
            elif token == '/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))
        
        return stack[0]
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for token in tokens:
            if token == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif token == "-":
                # The second pop is the left number: (second_pop - first_pop)
                b, a = num_stack.pop(), num_stack.pop()
                num_stack.append(a - b)
            elif token == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif token == "/":
                # The second pop is the left number: (a / b)
                b, a = num_stack.pop(), num_stack.pop()
                # Use int() for truncation toward zero as per LeetCode rules
                num_stack.append(int(a / b))
            else:
                # If it's a number, just push it
                num_stack.append(int(token))
                
        return num_stack[0]
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        par_match = {"}": "{", "]" : "[", ")": "("}

        for c in s:
            if c in par_match :
                if not my_stack or my_stack[-1] != par_match[c]:
                    return False
                elif my_stack:
                    my_stack.pop()
            else:
                my_stack.append(c)
        return not my_stack

        
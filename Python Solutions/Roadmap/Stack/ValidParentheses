class Solution:
    def isValid(self, s) -> bool:
        stack = []

        for st in s:
            # Check if empty
            if not stack:
                stack.append(st)
                continue

            # Check if opening bracket
            if st in ["{", "(", "["]:
                stack.append(st)
                continue

            # Check if closing bracket
            if st in ["}", ")", "]"]:
                # Compare to top of stack
                top = stack.pop()

                if ( st == ")" and top == "(" ) or ( st == "}" and top == "{" ) or ( st == "]" and top == "[" ) :
                    # Valid check
                    continue
                else:
                    return False

        # Check if stack empty
        return not stack

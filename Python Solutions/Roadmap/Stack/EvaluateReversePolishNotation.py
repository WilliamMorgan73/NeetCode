class Solution:
    def evalRPN(self, tokens) -> int:
        
        num_stack = []

        for token in tokens:
            # Check if token is a number
            if token not in ["+", "-", "*", "/"]:
                num_stack.append(token)
            else:
                
                num2 = num_stack.pop()
                num1 = num_stack.pop()

                if token == "/":
                    # Perform integer division
                    result = int(eval(f'{num1} {token} {num2}'))
                else:
                    # Perform other operations
                    result = eval(f'{num1} {token} {num2}')
                    
                num_stack.append(str(result))

        return int(num_stack[0])
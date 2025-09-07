class Solution:
    def dailyTemperatures(self, temperatures):
        
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            current_temp = temperatures[i]
            
            # Pop until we find a warmer temperature
            while stack and temperatures[stack[-1]] <= current_temp:
                stack.pop()

            # If theres a warmer day ahead, calculate how far
            if stack:
                output[i] = stack[-1] - i

            # Push this days index onto stack
            stack.append(i)

        return output
            
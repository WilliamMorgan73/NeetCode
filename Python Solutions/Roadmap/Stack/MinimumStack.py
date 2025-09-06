class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # Now for min stack
        # We don't need to keep track of all elements, all we need to do is keep track of the min at that time
        # As if something larger is pushed, the min wont change as it would be popped before it would come up as the new min

        # Therefore we can just append to min stack the smallest of val or minstack top

        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()

        # Also pop for min stack
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

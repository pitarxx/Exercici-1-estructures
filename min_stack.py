class MinStack:

    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        if self._stack:
            current_min = self._stack[-1][1]
            new_min = val if val < current_min else current_min
        else:
            new_min = val
        self._stack.append((val, new_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]

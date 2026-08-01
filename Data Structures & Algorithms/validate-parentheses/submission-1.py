class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        match = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if len(stack) == 0 or stack[-1] != match[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
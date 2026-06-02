class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = deque()
        for i in tokens:
            if(i.isdigit()):
                stack.append(int(i))
            elif(i=="+"):
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif(i=="-"):
                a=stack.pop()
                b=stack.pop()
                stack.append(a-b)
            elif(i=="*"):
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif(i=="/"):
                a=stack.pop()
                b=stack.pop()
                stack.append(b/a)
        return stack.pop()
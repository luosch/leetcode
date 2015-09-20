class Solution(object):
    def calculate(self, s):
        s = s.replace(" ", "")
        ops = {"+", "-", "(", ")"}
        inOrder = []
        postOrder = []
        stack = []
        cursor = 0
        tmp = -1
        
        # transform string to inOrder list
        for cursor in range(0, len(s)):
            if s[cursor] in ops:
                if tmp != -1:
                    inOrder.append(tmp)
                    tmp = -1
                inOrder.append(s[cursor])
            elif not s[cursor] in ops:
                if tmp == -1:
                    tmp = int(s[cursor])
                else:
                    tmp = tmp * 10 + int(s[cursor])
        
        if tmp != -1:
            inOrder.append(tmp)

        # transform inOrder list to postOrder list
        for item in inOrder:
            if isinstance(item, int):
                print(item)
                postOrder.append(item)
            else:
                if item == "+" or item == "-":
                    while stack and stack[-1] != "(":
                        postOrder.append(stack.pop())
                    stack.append(item)
                elif item == "(":
                    stack.append(item)
                elif item == ")":
                    while stack and stack[-1] != "(":
                        postOrder.append(stack.pop())
                    stack.pop()
        
        while stack:
            postOrder.append(stack.pop())

        # calculate postOrder list
        for item in postOrder:
            if item == "+":
                stack[-2] = stack[-2] + stack[-1]
                stack.pop()
            elif item == "-":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop()
            else:
                stack.append(item)

        return stack[0]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(y+x)    
            elif i == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
               
            elif i == '*':
                x = stack.pop()
                y = stack.pop()
                stack.append(y*x)
                
            elif i == '/':
                x = stack.pop()
                y = stack.pop()
                if x < 0 or y < 0:
                    if x < 0  and y < 0:
                        stack.append(y//x)
                    else:
                        stack.append(ceil(y/x))
                
                else:
                    stack.append(y//x)
            else:
                stack.append(int(i))
      
        return stack.pop()
                
            
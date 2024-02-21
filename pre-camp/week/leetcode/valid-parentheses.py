class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        count=0
        stack=[]
        while i < len(s):
            if s[i]=='(' or s[i]=='[' or s[i]=='{' :         
                stack.append(s[i])
                i=i+1
            else: 
                if s[i]==')' :
                    if len(stack)!=0 and stack[len(stack)-1]=='(':
                        stack.pop()
                        i=i+1
                    else:
                        return False
                elif s[i]==']': 
                    if len(stack)!=0 and stack[len(stack)-1]=='[':
                        stack.pop()
                        i=i+1
                    else:
                        return False
                elif s[i]=='}' :
                    if len(stack)!=0 and stack[len(stack)-1]=='{':
                        stack.pop()
                        i=i+1
                    else:
                        return False
                
        if len(stack)==0:
            return True
        else:
            return False

     

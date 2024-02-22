class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for i in path:
            if i == "." or i == "" :
                pass
            elif stack and  i == "..": 
                stack.pop()
            elif i != "." and i != ".." :
                stack.append("/" + i)
               
        if len(stack) == 0:
            stack.append("/")
        return "".join(stack)
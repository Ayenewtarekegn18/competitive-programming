class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False
        i=0
        j=0

        while j < len(typed):

            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False

        return i == len(name)
            
      
        
        
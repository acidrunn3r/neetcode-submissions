class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if stack == []:
                    return False
                match char:
                    case "}":
                        if stack[-1] != "{": 
                            return False
                        else:
                            stack.pop()
                        
                    case ")":
                        if stack[-1] != "(": 
                            return False
                        else:
                            stack.pop()
                    
                    case "]":
                        if stack[-1] != "[": 
                            return False
                        else:
                            stack.pop()
            
        return stack == []

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic:
                if stack and dic[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
        return len(stack) == 0
            

            

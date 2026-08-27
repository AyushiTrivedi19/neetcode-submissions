class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(','}':'{',']':'['}
        for i in s:
            if i in pairs:
                if len(stack)==0 or stack.pop() != pairs[i]:
                    return False
            else:
                stack.append(i)
        if len(stack)==0:
            return True
        else:                
            return False
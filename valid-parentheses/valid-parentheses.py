class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        self.stack = []
        self.dict={"]":"[",")":"(","}":"{"}
        for i in s:
            if i in ("(","[","{"):
                self.stack.append(i)
            if i in (")","]","}"):
                if len(self.stack) == 0:
                    return False
                if not self.stack.pop() == self.dict[i]:
                    return False
        if  len(self.stack) == 0:
            return True
        else: return False
            
class Solution:
    def romanToInt(self, s: str) -> int:
        self.dict = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        self.len = len(s)
        self.total = 0
        i = 0
        while i <= self.len - 1:
            if s[i:i+2] in self.dict.keys():
                self.total += self.dict[s[i:i+2]]
                i += 2
            else:
                self.total += self.dict[s[i]]
                i += 1
        return self.total
    # code complexity is O(n)
    # storage complexity is O(1)
                
        
        
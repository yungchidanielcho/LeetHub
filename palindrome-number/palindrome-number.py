class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x_str = str(x)
        self.len = len(self.x_str)
        self.range = range(self.len,0,-1)
        self.list = [self.x_str[i-1] for i in self.range]
        self.rev_str = "".join(self.list)
        if self.x_str == self.rev_str:
            return True
        else: return False
        # algorithmic complexity O(n)
        # algorithmic complexity O(1)
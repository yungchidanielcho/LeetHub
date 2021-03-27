class Solution:

    def reverse(self, x: int) -> int:
        if x < 0:
            x = abs(x)
            self.sign = -1
        else: self.sign = 1
        self.str = str(x)
        self.len = len(self.str)
        self.rev_idx = range(self.len,0,-1)
        self.rev_list = [self.str[i-1] for i in self.rev_idx]
        self.rev_num = self.sign * int("".join(self.rev_list))
        if self.rev_num in range(-2**31,2**31 - 1):
            return self.rev_num
        else:
            return 0
    
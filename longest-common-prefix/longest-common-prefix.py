class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # check if list is empty
        if len(strs) == 0:
            return ""
        self.strs = strs
        # check if string is empty
        if len(strs[0]) == 0:
            return ""
        self.str = strs[0]
        self.prefix = ""
        for i in range(len(self.str)+1):
            self.prefix_temp = self.str[:i]
            if all(map(lambda x: x.startswith(self.prefix_temp),self.strs)):
                self.prefix = self.prefix_temp
            else:
                return self.prefix
        return self.prefix
        # algorithmic complexity is O(n)
        # storage complexity is O(1)


                
                
                
                
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = []
        for i in range(len(s)):
            if s[i].isalnum():
                s1.append(s[i].lower())
        s2 = list(reversed(s1))
        return s1 == s2
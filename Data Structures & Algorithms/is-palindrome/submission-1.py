class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        pal = []

        for c in s:
            if c.isalnum():
                temp.append(c.lower())
        
        normal = temp.copy()
        
        while (len(temp) > 0):
            pal.append(temp.pop())
        
        if pal == normal:
            return True
        else:
            return False


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += str(length) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded = []
        prev = 0
        curr = 0
        num = 0
        length = len(s)

        while curr < len(s):
            if s[curr] == '#':
                num = int(s[prev:curr])
                curr += 1
                decoded.append(s[curr:curr+num])
                curr += num
                prev = curr
            curr += 1
        
        return decoded

        
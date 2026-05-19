class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
                return []
        res = []
        len_p = len(p)

        target = [0] * 26
        window = [0] * 26

        for c in p:
            target[ord(c) - 97] += 1

        for i in range(len(s)):
            window[ord(s[i]) - 97] += 1

            if i >= len_p:
                window[ord(s[i - len_p]) - 97] -= 1

            if window == target:
                res.append(i - len_p + 1)

        return res
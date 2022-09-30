class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_table = {}
        t_table = {}
        if len(s) != len(t):
            return False
        for char in range(len(s)):
            if s[char] in s_table:
                s_table[s[char]] += 1
            else:
                s_table[s[char]] = 1
            if t[char] in t_table:
                t_table[t[char]] += 1
            else:
                t_table[t[char]] = 1
        
        return s_table == t_table
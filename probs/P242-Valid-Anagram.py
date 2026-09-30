class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] = s_map[i] + 1

        
        for i in t:
            if i not in t_map:
                t_map[i] = 1
            else:
                t_map[i] = t_map[i] + 1

        return s_map == t_map
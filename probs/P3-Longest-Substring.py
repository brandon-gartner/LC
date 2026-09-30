class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_c = set()
        length = 0
        lo = 0
        hi = 0
        while (hi < len(s)):
            if s[hi] not in set_c:
                set_c.add(s[hi])
                length = max(length, hi - lo + 1)
            else:
                while (s[hi] in set_c):
                    set_c.remove(s[lo])
                    lo += 1
                set_c.add(s[hi])
            
            hi += 1

        return length
        
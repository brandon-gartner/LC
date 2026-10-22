class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer question, start looking at both edges, go closer and closer until r < l. if it was always the same, return True! else return false
        # edge cases take 1:
        #   - size 0 -> return True
        #   - size 1 -> return True
        # had to look up -> uppercase to lowercase function, how to filter for alphanumerics only

        if len(s) == 0:
            return True

        s = "".join(filter(str.isalnum, s)).lower()
        
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False

            else:
                l += 1
                r -= 1

        return True
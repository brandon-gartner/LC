class Solution:
    def isValid(self, s: str) -> bool:
        # contains [, ], {, }, (, )
        # return true  if valid parentheses, false otherwise
        if len(s) % 2 != 0:
            return False
            
        stack = deque()
        for i in range(len(s)):
            match s[i]:
                case '(' | '{' | '[':
                    stack.append(s[i])
                case ')' | '}' | ']':
                    if len(stack) == 0:
                        return False
                    
                    c = stack.pop()
                    bracket_mismatch = c != '(' and s[i] == ')'
                    curly_mismatch = c != '{' and s[i] == '}'
                    square_mismatch = c != '[' and s[i] == ']'
                    if bracket_mismatch or curly_mismatch or square_mismatch:
                        return False

        return True if len(stack) == 0 else False
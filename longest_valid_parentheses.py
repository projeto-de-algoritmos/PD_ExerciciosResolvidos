## https://leetcode.com/problems/longest-valid-parentheses/
def longestValidParentheses(s: str) -> int:
    n = len(s)
    stk = []
    stk.append(-1)
    result = 0
    for i in range(n):
        # If opening bracket, push index of it
        if s[i] == '(':
            stk.append(i)
        else:  
            if len(stk) != 0:
               stk.pop()
            if len(stk) != 0:
                result = max(result,
                             i - stk[len(stk)-1])
            else:
                stk.append(i)
    return result

string = "((()()"
print (longestValidParentheses(string))
 
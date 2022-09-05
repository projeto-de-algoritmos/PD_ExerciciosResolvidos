## https://leetcode.com/problems/different-ways-to-add-parentheses/
def diffWaysToCompute(self, expression: str) -> List[int]:
        expr = ''
        numbers = re.split("[* + -]",expression)
        for i in expression:
            if i.isalnum() == False:
                expr+=i

        n = len(numbers)
        dp = [[[]]*(n+1) for i in range(n+1)]
        for i in range(n):
            dp[i][i] = [int(numbers[i])]


        for gap in range(1, n):
                i = 0
                for j in range(gap, n):
                    for g in range(gap):
                        k = i + g
                        temp = []+dp[i][j]
                        if expr[k] == '-':
                            for l in dp[i][k]:
                                for o in dp[k+1][j]:
                                    temp.append(l-o)

                        if expr[k] == '*':
                            for l in dp[i][k]:
                                for o in dp[k+1][j]:
                                    temp.append(l*o)
                        if expr[k] == '+':
                            for l in dp[i][k]:
                                for o in dp[k+1][j]:
                                    temp.append(l+o)
                        dp[i][j] = temp
                    i+=1
        return dp[0][n-1]
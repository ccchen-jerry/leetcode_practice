class Solution:
    def value(symbol):
        if (symbol == 'I'):
            return 1
        if (symbol == 'V'):
            return 5
        if (symbol == 'X'):
            return 10
        if (symbol == 'L'):
            return 50
        if (symbol == 'C'):
            return 100
        if (symbol == 'D'):
            return 500
        if (symbol == 'M'):
            return 1000
        return -1

    def romanToInt(self, s: str) -> int:
        if len(s) < 1:
            return 0
        elif len(s) == 1:
            return Solution.value(s)
        else:
            result = Solution.value(s[0])
            for i in range(1, len(s)):
                if Solution.value(s[i - 1]) > Solution.value(s[i]):
                    result += Solution.value(s[i])
                else:
                    result -= Solution.value(s[i - 1])
                    result += Solution.value(s[i]) - Solution.value(s[i - 1])
            return result


'''
# solution from the internet
roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000
     

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        n = len(s)

        i = 0
        while i < n :

            # If present value is less than next value,
            # subtract present from next value and add the
            # resultant to the sum variable.
            # print(roman[s[i]],roman[s[i+1]])
            if (i != n - 1 and roman[s[i]] < roman[s[i + 1]]):
                sum += roman[s[i + 1]] - roman[s[i]]
                i += 2
                continue
            else:
                sum += roman[s[i]]
            i += 1
        return sum
'''
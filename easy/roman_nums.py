
'''
Roman numerals are represented by seven different symbols 
I, V, X, L, C, D and M

I     1
V     5
X     10
L     50
C     100
D     500
M     1000

Roman numerals are usually written largest to smallest from left to right.
However the numeral for four is not IIII. Insted the number four is written
as IV. Because the one is before the five we subtract it making four.
The same principle applies to number nine, which is written IX

* 'I' can be placed before V(5) and X(10) to make 4 and nine
* 'X' can be placed before L(50) and C(100) to make 40 and 90
* 'C' can be placed before D(500) and M(1000) to make 400, 

Given a roman numeral, convert it to the integer

example
s = 'III'
output: 3

s = 'LVIII'
output: 58
'''

class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0 
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total + roman[s[-1]]

solution = Solution()
s = 'CCX'
result = solution.romanToInt(s)
print(result)

'''
Given a signed a 32 bit integer x, return x with its digits reversed. If reversing x
causes the value to go outside the signed 32 bit integer range then return 0

Input x = 123
Output 321

Input -123
Output -321

Input 120
Output 21


'''

# Option 1
class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0

        if x < -2**31 or x > 2**31 - 1:
            return 0

        is_negative = False

        if x < 0:
            is_negative = True
            x = abs(x)
            
        if x % 2 != 0:
            num_str = str(x)[::-1]

        else:
            num_str = str(x).rstrip('0')[::-1]

        result = int(num_str)

        if result < -2**31 or result > 2**31 - 1:
            return 0

        if is_negative:
            result = -result
            
        return result
    

# Option 2


# def convert(integer):
#     if integer > 0:
#         if integer % 2 != 0:
#             num = str(integer)[::-1]
#             return int(num)
#         else:
#             num = int(str(integer).rstrip('0'))
#             res = int(str(num)[::-1])
#             return res
#     elif integer == 0:
#             return 0
#     else:
#         num = abs(integer)
#         num = str(num)[::-1]
#         num = -abs(int(num))
#         return num

# result = convert((123))
# print(type(result))









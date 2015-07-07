import copy

class Solution:
    # @param {string} str
    # @return {integer}
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    def myAtoi(self, str):
        try:
            str = str.strip()

            for i in range(0, len(str)):
                if not ('0' <= str[i] <= '9' or str[i] == '+' or str[i] == '-'):
                    str = str[0:i]
                    break

            num = int(str)
            if num > 2147483647:
                return 2147483647
            elif num < -2147483648:
                return -2147483648
            else:
                return num

        except Exception, e:
            return 0

hi = Solution()

test_case1 = ['', "123", "00", "-01", "-1", "asd", "123d", "##", "a",
              '   12', '12     ', '    +2', '+-2', '+2',
              "21474836470", "-122147483647", "2147483647", "-2147483648",
              "  12s", "  s23", "12s sda23","123 34"
              ]  # common


for item in test_case1:
    print "Input:", item, " output:", hi.myAtoi(item)

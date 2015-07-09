class Solution:
    # @param {integer} num  1-3999
    # @return {string}
    def intToRoman(self, num):
        result = ''

        thousands = num/1000
        result += 'M' * thousands
        num %= 1000

        hundreds = num/100
        result += self.attach(hundreds, 'M', 'D', 'C')
        num %= 100

        tens = num/10
        result += self.attach(tens, 'C', 'L', 'X')
        num %= 10

        units = num
        result += self.attach(units, 'X', 'V', 'I')

        return result

    def attach(self, count, sign_10, sign_5, sign_1):
        result = ''
        if count == 9:
            result += sign_1 + sign_10
        elif count == 4:
            result += sign_1 + sign_5
        else:
            if count >= 5:
                result += sign_5
                count -= 5
            result += sign_1 * count
        return result


hi = Solution()

test_case = [
    1, 4, 5, 6, 9, 10, 1437, 3999

]  # common

for item in test_case:
    print "Input:", item, " output:", hi.intToRoman(item)


# I?1??V?5??X?10??L?50??C?100??D?500??M?1000?
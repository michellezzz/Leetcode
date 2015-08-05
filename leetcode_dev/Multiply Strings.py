class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    block_size = 3

    def seg(self, num):

        if len(num) <= self.block_size:
            return "", num
        else:
            return num[:-self.block_size], num[-self.block_size:]


    def add_str(self, num1, num2):
        carry = 0
        i = len(num1)-1
        j = len(num2)-1
        result = ''
        while i >= 0 or j >= 0 or carry != 0:
            tmp = carry
            if i>=0:
                tmp += int(num1[i])
            if j>=0:
                tmp += int(num2[j])
            result = str(tmp % 10) + result
            carry = tmp/10
            i -= 1
            j -= 1
        return result

    def multiply(self, num1, num2):
        a1, b1 = self.seg(num1)
        a2, b2 = self.seg(num2)

        if len(a1) == 0 and len(a2) == 0:
            if len(b1) == 0 or len(b2) == 0:
                return ''
            else:
                return str(int(b1)*int(b2))
        else:
            tmp1 = self.multiply(a1, a2) + '0' * (self.block_size*2)
            tmp2 = self.multiply(a1, b2) + '0' * (self.block_size)
            tmp3 = self.multiply(a2, b1) + '0' * (self.block_size)
            tmp4 = self.multiply(b1, b2)
            return self.add_str(self.add_str(tmp2, tmp3), self.add_str(tmp1, tmp4))


hi = Solution()

test_case = [
    ("12", "123"),
    ("12345","1231351246147"),
    ("1","1"),
    ('99', "9999"),
    ("9999",'1'),
    ('0','00'),
    ('','')
    ]# common

for item in test_case:
    print "Input:", item, " output:\n", hi.add_str(item[0], item[1])






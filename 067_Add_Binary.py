class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        tmp_len = max(len(a), len(b)) + 1
        a = '0' * (tmp_len - len(a)) + a
        b = '0' * (tmp_len - len(b)) + b 
        result = ''
        carry = 0
        for i in range (0, tmp_len):
            tmp1 = int(a[-(i+1)])
            tmp2 = int(b[-(i+1)])
            tmp_sum = tmp1 + tmp2 + carry
            if tmp_sum == 0:
                x = '0'
                carry = 0
            elif tmp_sum == 1:
                x = '1'
                carry = 0
            elif tmp_sum == 2:
                x = '0'
                carry = 1
            elif tmp_sum == 3:
                x = '1'
                carry = 1
            result = x + result
        if result[0] == '0':
            return result[1:]
        else:
            return result


hi = Solution()
print hi.addBinary("1101", "1001")
print hi.addBinary("1101", "")
print hi.addBinary("1111", "1111")
        


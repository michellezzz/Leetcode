class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        num = str(1)
        for i in range (0, n-1):
            new_num = ''
            ####################
            num += 'x'
            last = num[0]
            count = 1
            for j in range (1, len(num)):
            
                this = num[j]
                if this == last:
                    count += 1
                else:
                    new_num += str(count) + last
                    count = 1
                last = this
    
            #################### 
            num = new_num

        return num
                


hi = Solution()
print hi.countAndSay(2)
            

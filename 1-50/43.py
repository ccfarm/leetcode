class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def num_to_list(num):
            l = list(num)
            l.reverse()
            l = list(map(lambda x: int(x), l))
            return l
        n1 = num_to_list(num1)
        n2 = num_to_list(num2)
        ans = [0 for _ in range(300)]
        for i in range(len(n1)):
            for j in range(len(n2)):
                x = n1[i] * n2[j]
                ans[i + j] += x % 10
                ans[i + j + 1] += x // 10
        st = ""
        for i in range(299):
            ans[i + 1] += ans[i] // 10
            ans[i] %= 10
        i = 299
        while i >= 0 and ans[i] == 0:
            i -= 1
        if i == -1:
            return "0"
        while i >= 0:
            st = st + str(ans[i])
            i -= 1
        return st
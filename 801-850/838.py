class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        flag = 0
        i = 0
        j = -1
        le = len(dominoes)
        ans = ""
        while i < le:
            if dominoes[i] == 'L':
                if flag == 0:
                    ans = ans + 'L' * (i-j)
                else:
                    flag = 0
                    gap = j - i
                    ans = ans + 'L' * (gap // 2) + '.' * (gap % 2) + 'R' * (gap // 2);
                j = i
            elif dominoes[i] == 'R':
                if flag == 0:
                    flag = 1
                else:
                    ans = ans + ans + 'R' * (i-j - 1)
                    j = i - 1
            i += 1
        if flag == 1:
            ans = ans + 'R' * (le - 1 - j)
        return ans
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        def dfs(k, now, s):
            if k == 4:
                if int(s) in range(256) and (len(s) == 1 or s[0] != '0'):
                    ans.append(now + "." + s)
            else:
                if k != 1:
                    now = now + '.'
                l = len(s)
                dfs(k + 1, now + s[0], s[1:])
                if s[0] != '0':
                    if l - 2 >= 4 - k:
                        dfs(k + 1, now + s[:2], s[2:])
                    if l - 3 >= 4 - k:
                        dfs(k + 1, now + s[:3], s[3:])
        dfs(1, '', s)
        return ans
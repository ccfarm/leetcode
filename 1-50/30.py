class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        dd = {}
        for key in words:
            dd[key] = words.count(key)
        if words == []:
            return []
        l = len(words[0])
        n = len(words)
        ans = []
        for i in range(len(s) - l * n + 1):
            for j in range(n):
                d = dd.copy()
                st = s[i + j * l: i + j * l + l]
                if st in d and d[st] > 0:
                    d[st] -= 1
                else:
                    break
            else:
                print(dd)
                ans.append(i)
        return ans
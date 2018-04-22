class Solution:
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        st = ""
        words.sort(key = len)
        i = len(words) - 1
        ans = 0
        s = set()
        while i >= 0:
            if words[i] not in s:
                ans += len(words[i]) + 1
            else:
                for i in range(len(words[i])):
                    s.add(words[i:])
            i -= 1
        return ans
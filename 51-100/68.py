class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        i = 0
        ans = []
        while i < len(words):
            sum = len(words[i])
            j = 1
            while i + j < len(words) and sum + len(words[i + j]) + 1 <= maxWidth:
                sum += len(words[i + j]) + 1
                j += 1
            remain = maxWidth - sum
            if j == 1:
                ans.append(words[i] + ' ' * remain)
                i += j
                continue
            space = remain // (j - 1) + 1
            space1 = remain % (j - 1)

            k = 0
            line = ""
            if i + j == len(words):
                while k < j - 1:
                    line = line + words[i + k] + ' '
                    k += 1
                line = line + words[-1] + ' ' * remain
                ans.append(line)
                return ans
            while k < j - 1:
                line = line + words[i + k] + ' ' * space
                if k < space1:
                    line = line + ' '
                k += 1
            line = line + words[i + j - 1]
            ans.append(line)
            i += j
        return ans

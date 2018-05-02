class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return []
        else:
            wordList.remove(endWord)
        if beginWord in wordList:
            wordList.remove(beginWord)
        wordList.insert(0, beginWord)
        wordList.append(endWord)

        l1 = len(beginWord)
        l = len(wordList)

        d = {}

        for word in wordList:
            for k in range(l1):
                tmp = word[:k]+'_'+word[k+1:]
                d[tmp] = d.get(tmp, []) + [word]

        s = set()
        q = [[word[0]]]

        flag = 0
        while q:
            p = []
            for words in q:
                s1 = set()
                if words[-1] == endWord:
                    flag = 1
                    break
                for k in range(l1):
                    tmp = words[-1][:k]+'_'+words[-1][k+1:]
                    for neib in d[tmp]:
                        if neib not in s:
                            s1.add(neib)
                            p.append(words + [neib])
                s = s | s1
            q = p

            ans = []
            if flag == 1:
                for words in q:
                    if words[-1] == endWord:
                        ans.append(words)
                return ans

        return []
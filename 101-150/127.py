from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
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
        q = [word[0]]

        ans = 1;
        while q:
            p = []
            for word in q:
                s.add(word)
                if word == endWord:
                    return ans
                for k in range(l1):
                    tmp = word[:k]+'_'+word[k+1:]
                    for neib in d[tmp]:
                        if neib not in s:
                            p.append(neib)
            q = p
            ans += 1
        return 0

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        q = wordlist.copy()
        while q:
            temp = q.pop()
            nn = master.guess(temp)
            if nn == 6:
                break
            p = []
            for x in q:
                count = 0
                for i in range(6):
                    if x[i] != temp[i]:
                        count += 1
                if count == nn:
                    p.append(x)
            q = p
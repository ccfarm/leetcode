class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = S.split(' ')
        vow = set(['a', 'e' , 'i' ,'o' ,'u','A','E','I','O','U'])
        for i, word in enumerate(1, l):
            if word[0] in vow:
                word = word + "ma"
            else:
                word = word[1:] + word[0] + "ma"
            word = word + "a"*(i)
        return " ".join(word)


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def perse(ver):
            l = ver.split('=')[1]
            l.replace(' ', '').replace('"', '')
            l = l.split('.')
        l1 = perse(version1)
        l2 = perse(version2)
        print(l1)
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        arr = list(zip(difficulty, profit))
        arr.sort(key=lambda x: x[1], reverse=True)
        worker.sort(reverse=True)

        ans = 0
        l = len(arr)
        i = 0
        for x in worker:
            while i < l and arr[i][0] > x:
                i += 1
            if i < l:
                ans += arr[i][1]
        return ans
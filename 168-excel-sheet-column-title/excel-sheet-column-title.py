class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            res = chr(remainder + ord('A'))+res
            columnNumber //=26
        return res
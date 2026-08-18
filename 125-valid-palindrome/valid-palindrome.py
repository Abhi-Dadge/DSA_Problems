class Solution(object):
    def isPalindrome(self, s):
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean+=ch.lower()
        rev = clean[::-1]
        return clean == rev
           
    

        
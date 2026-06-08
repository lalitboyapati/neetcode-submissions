class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        cleanss = ""
        arr = s.split(" ")
        for x in arr:
            ss += x
        for i in range(len(ss)):
            if ss[i].isalnum() == True:
                cleanss += ss[i].lower()
        if cleanss == cleanss[::-1]: return True
        else: return False

        
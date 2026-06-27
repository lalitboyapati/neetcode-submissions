class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for x in s: 
            if x.isalnum(): news += x.lower()
        return news == news[::-1]

        
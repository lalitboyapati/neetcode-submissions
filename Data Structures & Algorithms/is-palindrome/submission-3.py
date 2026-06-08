class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleans = ""
        for ch in s:
            if ch.isalnum():
                cleans += ch.lower()
        return cleans == cleans[::-1]

        
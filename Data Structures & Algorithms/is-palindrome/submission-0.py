class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                alphanum += letter.lower()
        return alphanum == alphanum[::-1]
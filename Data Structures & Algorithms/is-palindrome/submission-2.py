class Solution:
    def isGoodChar(self, letter: str) -> bool:
        if (
            (ord('a') <= ord(letter) <= ord('z'))
            or (ord('A') <= ord(letter) <= ord('Z'))
            or (ord('0') <= ord(letter) <= ord('9'))
        ):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if not self.isGoodChar(s[left]):
                left += 1
            elif not self.isGoodChar(s[right]):
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1

        return True
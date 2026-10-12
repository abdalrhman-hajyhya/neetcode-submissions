class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        numberOfLetters = 26
        lettersInS = [0] * numberOfLetters
        lettersInT = [0] * numberOfLetters

        for letter in s:
            lettersInS[ord(letter) - ord("a")] += 1
        for letter in t:
            lettersInT[ord(letter) - ord("a")] +=1
        
        for letter in range(numberOfLetters):
            if lettersInS[letter] != lettersInT[letter]:
                return False

        return True 
        
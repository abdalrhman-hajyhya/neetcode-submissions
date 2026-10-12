class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_array = []
        for string in strs:
            stringInAscii = ""
            for letter in string:
                letterInAscii = str(ord(letter))
                stringInAscii = stringInAscii + letterInAscii + "a"
            stringInAscii += "b"
            encoded_array.append(stringInAscii)
        return("".join(encoded_array))
    def decode(self, s: str) -> List[str]:
        ans = []
        charInString = ""
        word = ""
        for letter in s:
            if letter == "a" and charInString != "":
                charInString = chr(int(charInString))
                word += charInString
                charInString = ""
            elif letter == "b":
                ans.append(word)
                word = ""
                charInString = ""
            else:
                charInString += letter 
        return ans
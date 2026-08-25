class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        pos = 0
        while pos<len(s):
            delimiter_index = s.find("#", pos)
            length = int(s[pos:delimiter_index])
            decoded.append(s[delimiter_index+1:delimiter_index+length+1])
            pos = delimiter_index+length+1
        return decoded


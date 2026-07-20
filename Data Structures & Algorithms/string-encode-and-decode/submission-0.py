class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            num_str = ""
            while s[i] != "#":
                num_str += s[i]
                i += 1
            
            i += 1

            out_str = ""
            for v in range(int(num_str)):
                out_str += s[i]
                i += 1

            output.append(out_str)

        return output

class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def decode(location: int):
            data = ""
            copies = ""
            while location != n:
                if s[location] == "[":
                    location, decoded_data = decode(location + 1)
                    if copies:
                        data += decoded_data * int(copies)
                        copies = ""
                    continue
                if s[location] == "]":
                    return location + 1, data
                if s[location].isalpha():
                    data += s[location]
                if s[location].isnumeric():
                    copies += s[location]
                location += 1
            return data, location

        decoded_data, location = decode(0)
        return decoded_data

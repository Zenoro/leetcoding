class Solution:
    def compress(self, chars: list[str]) -> int:
        if (len(chars) == 1):
            return 1
        counter = 1
        pointer = 1
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                counter += 1
            elif counter == 1:
                chars[pointer] = chars[i + 1]
                pointer += 1
            else:
                for digit in list(str(counter)):
                    chars[pointer] = digit
                    pointer += 1
                chars[pointer] = chars[i + 1]
                counter = 1
                pointer += 1
        if counter > 1:
            for digit in list(str(counter)):
                chars[pointer] = digit
                pointer += 1
        return pointer

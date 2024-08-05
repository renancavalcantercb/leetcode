class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev = 0
        for i in s:
            if prev < roman_dict[i]:
                result += roman_dict[i] - 2 * prev
            else:
                result += roman_dict[i]
            prev = roman_dict[i]
        return result

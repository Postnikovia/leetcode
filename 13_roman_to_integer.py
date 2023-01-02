class Solution:
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    replace_pair = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"], "M": [], "V": [], "L":[], "D":[]}

    def romanToInt(self, s: str) -> int:
        summ = 0
        i = 0
        while i < len(s)-1:
            if s[i+1] in self.replace_pair[s[i]]:
                summ += self.roman_dict[s[i+1]] - self.roman_dict[s[i]]
                i += 1
            else:
                summ += self.roman_dict[s[i]]
            i += 1
        if i < len(s):
            summ += self.roman_dict[s[i]]
        return summ


if __name__ == "__main__":
    print(Solution().romanToInt("MCMXCIV"))

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def base_case(s):
            value = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
            return value[s0] + self.romanToInt(s[1:])

        if s == "": return 0
        s0 = s[0]
        if s0 in {"C", "X", "I"} and len(s) > 1:
            s1 = s[1]
            if s0 + s1 == "CD":
                return 400 + self.romanToInt(s[2:])
            elif s0 + s1 == "CM":
                return 900 + self.romanToInt(s[2:])
            elif s0 + s1 == "XL":
                return 40 + self.romanToInt(s[2:])
            elif s0 + s1 == "XC":
                return 90 + self.romanToInt(s[2:])
            elif s0 + s1 == "IV":
                return 4 + self.romanToInt(s[2:])
            elif s0 + s1 == "IX":
                return 9 + self.romanToInt(s[2:])
            else:
                # identical with the base case
                return base_case(s)
        else:
            # identical with the base case
            return base_case(s)

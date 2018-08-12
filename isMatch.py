class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # Base Case:
        if s == "" and p == "":
            return True
        elif s == "":
            if len(p) > 1 and p[1] == "*":
                return self.isMatch(s, p[2:])
            else:
                return False
        elif p == "":
            return False
        # Cases are String vs Pattern

        s0 = s[0]
        p0 = p[0]
        if len(p) >= 2:
            # Case 1: char vs char + *
            if p0.islower() and p[1] == "*":
                if s0 == p0:
                    # it's possible that p0* is matching 0 or more
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s, p[2:])
            #     Case 2: char vs .*
            elif p0 == "." and p[1] == "*":
                if len(p) >= 3:
                    p3 = p[2]
                    if p3 != s0:
                        return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                    else:
                        return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
                else:
                    return True
            #     Case 3: char vs .
            elif p0 == ".":
                return self.isMatch(s[1:], p[1:])
            # Case 4: char vs char
            elif p0.islower():
                if s0 == p0:
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
        else:
            if len(s) != 1:
                return False
            else:
                return p0 == "." or p0 == s0


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Symbol       Value
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        # Special Cases: 4, 9, 40, 90, 400, 900

        ans = "M" * (num // 1000)
        num = num % 1000
        if num // 100 == 4:
            ans += "CD"
            num -= 400
        elif num // 100 == 9:
            ans += "CM"
            num -= 900
        else:
            ans += (num // 500) * "D"
            num = num % 500
            ans += (num // 100) * "C"
            num = num % 100

        if num // 10 == 4:
            ans += "XL"
            num -= 40
        elif num // 10 == 9:
            ans += "XC"
            num -= 90
        else:
            ans += (num // 50) * "L"
            num = num % 50
            ans += (num // 10) * "X"
            num = num % 10

        if num == 4:
            ans += "IV"
            num -= 4
        elif num == 9:
            ans += "IX"
            num -= 9
        else:
            ans += (num // 5) * "V"
            num = num % 5
            ans += num * "I"

        return ans

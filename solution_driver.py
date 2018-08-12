if __name__ == '__main__':
    from isMatch import Solution
    s = "aaaaaaaaaaab"
    p = "a*a*a*a*a*ab"
    sol = Solution()
    print(sol.isMatch(s, p))
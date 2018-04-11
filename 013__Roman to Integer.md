#13.Roman to Integer

Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

、、、
class Solution(object):
    def romanToInt(self, s):
        M = ["M", "MM", "MMM"]
        C = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        n = 0
        if s[:3] == M[2]:
            n = 1000 * 3 + n
            s = s[3:]
        elif s[:2] == M[1]:
            n = 1000 * 2 + n
            s = s[2:]
        elif s[:1] == M[0]:
            n = 1000 + n
            s = s[1:]
        else:
            n = n
        if s[:4] == "DCCC":
            n = 100 * 8 + n
            s = s[4:]
        elif s[:3] == "CCC":
            n = 100 * 3 + n
            s = s[3:]
        elif s[:3] == "DCC":
            n = 100 * 7 + n
            s = s[3:]
        elif s[:2] == "CC":
            n = 100 * 2 + n
            s = s[2:]
        elif s[:2] == "DC":
            n = 100 * 6 + n
            s = s[2:]
        elif s[:2] == "CD":
            n = 100 * 4 + n
            s = s[2:]
        elif s[:2] == "CM":
            n = 100 * 9 + n
            s = s[2:]
        elif s[:1] == "C":
            n = 100 * 1 + n
            s = s[1:]
        elif s[:1] == "D":
            n = 100 * 5 + n
            s = s[1:]
        else:
            n = n
        if s[:4] == "LXXX":
            n = 10 * 8 + n
            s = s[4:]
        elif s[:3] == "XXX":
            n = 10 * 3 + n
            s = s[3:]
        elif s[:3] == "LXX":
            n = 10 * 7 + n
            s = s[3:]
        elif s[:2] == "XX":
            n = 10 * 2 + n
            s = s[2:]
        elif s[:2] == "LX":
            n = 10 * 6 + n
            s = s[2:]
        elif s[:2] == "XL":
            n = 10 * 4 + n
            s = s[2:]
        elif s[:2] == "XC":
            n = 10 * 9 + n
            s = s[2:]
        elif s[:1] == "X":
            n = 10 * 1 + n
            s = s[1:]
        elif s[:1] == "L":
            n = 10 * 5 + n
            s = s[1:]
        else:
            n = n
        if s[:4] == "VIII":
            n = 8 + n
            s = s[4:]
        elif s[:3] == "III":
            n = 1 * 3 + n
            s = s[3:]
        elif s[:3] == "VII":
            n = 1 * 7 + n
            s = s[3:]
        elif s[:2] == "II":
            n = 1 * 2 + n
            s = s[2:]
        elif s[:2] == "VI":
            n = 1 * 6 + n
            s = s[2:]
        elif s[:2] == "IV":
            n = 1 * 4 + n
            s = s[2:]
        elif s[:2] == "IX":
            n = 1 * 9 + n
            s = s[2:]
        elif s[:1] == "I":
            n = 1 * 1 + n
            s = s[1:]
        elif s[:1] == "V":
            n = 1 * 5 + n
            s = s[1:]
        else:
            n = n
        return (n)
    def romanToInt(self, s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res
、、、

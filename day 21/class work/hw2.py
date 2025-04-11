

def xo(s):
    s = s.lower()
    if "o" not in s and "x" not in s:
        return True
    elif s.count("x") == s.count("o"):
        return True
    else:
        if s.count("x") != s.count("o"):
            return False


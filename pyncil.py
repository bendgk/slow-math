"""
Benjamin Kosten
A Python implementation of pencil and paper math.
Might be slow, but hopefully more powerful?
"""

class SlowMath:
    def modernize(self, x, y):
        while len(x) != len(y):
            if len(x) > len(y): y = "0" + y
            else: x = "0" + x

        return (x, y)

s = SlowMath()

print(s.modernize("1237", "38"))

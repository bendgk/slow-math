"""
Benjamin Kosten
A Python implementation of pencil and paper math.
Might be slow, but hopefully more powerful?
"""

class SlowMath:
    def standardize(self, x, y):
        while len(x) != len(y):
            if len(x) > len(y): y = "0" + y
            else: x = "0" + x

        return (x, y)

    def add(self, pair):
        x = pair[0][::-1]
        y = pair[1][::-1]

        remainder = 0
        out = ""
        
        for i in range(len(x)):
            b = str(int(x[i]) + int(y[i]) + remainder)
            if len(b) == 2:
                remainder = 1
                b = b[1]
            else: remainder = 0

            out = b + out

        return out

s = SlowMath()

num = "23738295234897589034759278"

for i in range(10000000):
   num = s.add((num, num))

print(num)

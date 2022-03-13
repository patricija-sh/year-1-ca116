#!/usr/bin/env python3

s = input()
total = ""

i = 0
while i < len(s):
    conversion = (s[i]1 * (2 ** i))
    total = total + conversion
    i = i + 1

print(total)

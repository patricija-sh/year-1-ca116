#!/usr/bin/env python3

s = input()

total = "0"

i = 0
while i < 10:
    j = 0
    while j < len(s) and s[j] != "+":
        j = j + 1
    print(s[:j] + s[j + 1:])
    i = i + 1

print(total)

#!/usr/bin/env python3

s = input()

i = 0
while i < 10:
    j = 0
    while j < len(s) and (s[j] != "+"):
        j = j + 1

    first_part = s[:j]
    second_part = s[j + 1:]

    print(int(first_part) + int(second_part))
    s = input()

    i = i + 1

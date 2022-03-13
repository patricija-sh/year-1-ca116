#!/usr/bin/env python3

s = input()
j = len(s) - 1

i = 0
while i < len(s) and (s[i] < "0" or s[i] > "9"):
    i = i + 1

if i < len(s):
    j = i
    while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
        j = j + 1

    print(s[i:j] + " " + str(i))

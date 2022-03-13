#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] < "0" or "9" < s[i]):
    i = i + 1

if i < len(s):
    j = i
    while j < len(s) and (s[j] >= "0" and s[j] <= "9"):
        j = j + 1
        k = j
        while k < len(s) and (s[k] < "0" or "9" < s[k]):
            k = k + 1
            i = k
            while i < len(s) and(s[i] >= "0" and s[i] <= "9"):
                i = i + 1

    print(s[k:i] + " " + str(k))

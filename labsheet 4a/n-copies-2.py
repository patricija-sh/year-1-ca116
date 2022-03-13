#!/usr/bin/env python3

s = input()
n = int(input())
hyphen = "-"

hyphenated = ((s + hyphen) * n)

print(hyphenated[0:-1])

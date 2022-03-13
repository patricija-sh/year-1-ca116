#!/usr/bin/env python3

x = int(input())

DD = ((x // 10000) * 100)

MM = ((((x % 100000) % 10000) // 100) * 10000)

YY = (x % 100)

print(MM + DD + YY)

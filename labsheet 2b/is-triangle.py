#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if (b >= a + c):
   print("no")
elif (a >= b + c):
   print("no")
elif (c >= a + b):
   print("no")
else:
   print("yes")

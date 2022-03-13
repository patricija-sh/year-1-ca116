#!/usr/bin/env python3

n = int(input())
while n != 0:
   curr = int(input())
   if n < curr and curr != 0:
      print("higher")
   elif curr == n and curr != 0:
      print("equal")
   elif n > curr and curr != 0:
      print("lower")
   n = curr

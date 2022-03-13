#!/usr/bin/env python3

s = input()
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

i = 0
while i < len(s):
   j = 0
   while j < len(capital_letters):
      if s[i] == capital_letters[j]:
         first_capital_letter = s[i]
         print(first_capital_letter)
         j = len(capital_letters)
         i = len(s)
      j = j + 1
   i = i + 1

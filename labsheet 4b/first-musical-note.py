#!/usr/bin/env python3

s = input()
notes = "abcdefg"
first_note = ""

i = 0
while i < len(s):
   j = 0
   while j < len(notes):
      if s[i] == notes[j]:
         first_note = s[i]
         print(first_note)
         j = len(notes)
         i = len(s)
      j = j + 1
   i = i + 1

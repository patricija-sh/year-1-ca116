#!/usr/bin/env python3

x = int(input())

first_middle_digit = ((((x % 100000) % 10000) // 1000) * 10)

second_middle_digit = ((((x % 100000) % 10000) % 1000) // 100)

middle_two_digits = first_middle_digit + second_middle_digit

print(middle_two_digits)

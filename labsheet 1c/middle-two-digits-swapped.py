#!/usr/bin/env python3

x = int(input())

first_middle_digit = (((x % 100000) % 10000) // 1000)

second_middle_digit = (((((x % 100000) % 10000) % 1000) // 100) * 10)

middle_two_digits_swapped = first_middle_digit + second_middle_digit

print(middle_two_digits_swapped)

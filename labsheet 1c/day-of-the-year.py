#!/usr/bin/env python3

month = int(input())
day_of_month = int(input())

day_of_year = (((month - 1) * 30) + day_of_month)

print(day_of_year)

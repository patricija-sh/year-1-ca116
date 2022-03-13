#!/usr/bin/env python3

month = int(input())
day_of_month = int(input())

day_of_week = (((month - 1) * 30) + day_of_month - 1) % 7 + 1

print(day_of_week)

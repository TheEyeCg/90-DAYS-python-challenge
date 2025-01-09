#!/usr/bin/env python3

# Countdown using a while loop
print("Countdown using while loop:")
count = 10  # Start from 10
while count > 0:
    print(count)
    count -= 1  # Decrease the count by 1

# Countdown using a for loop
print("\nCountdown using for loop:")
for num in range(10, 0, -1):  # Start at 10, stop before 0, decrement by 1
    print(num)

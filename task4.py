# Find numbers divisible by 7 and multiples of 5
result = []

for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        result.append(str(num))

# Display result
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:")
print(', '.join(result))

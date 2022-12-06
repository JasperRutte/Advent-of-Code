numbers = []
x = 0
top_three = 0

calories = open("elf-calories", "r").read()

z = calories.split("\n")

for nummer in z:
    if nummer == "":
        numbers.append(x)
        x = 0
    else:
        x += int(nummer)

numbers.sort(reverse=True)
for i in range(0, 3):
    top_three += numbers[i]

print(top_three)
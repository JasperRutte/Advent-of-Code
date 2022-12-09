import string

items = open("rucksack-items.txt").read()
containment_sort = items.split("\n")
repeated = []
uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
sum_priority = 0

x = False

for amount in containment_sort:
    print(amount)
    half = slice(len(amount) // 2)
    other_half = slice(len(amount) // 2, len(amount))
    for letters in amount[half]:
        for other_letters in amount[other_half]:
            if letters == other_letters:
                repeated.append(other_letters)
                x = True
                break
        if x:
            x = False
            break

print(uppercase)
print(lowercase)

for items in repeated:
    priority = 1
    for letters in lowercase:
        if items == letters:
            sum_priority += priority
            priority = 1
        else:
            priority += 1
    priority = 27
    for letters in uppercase:
        if items == letters:
            sum_priority += priority
            priority = 27
        else:
            priority += 1

print(sum_priority)
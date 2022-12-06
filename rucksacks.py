items = open("rucksack-items.txt").read()
containment_sort = items.split("\n")
repeated = []

for amount in containment_sort:
    print(amount)
    half = slice(len(amount)//2)
    other_half = slice(len(amount)//2, len(amount))
    for letters in amount[half]:
        for other_letters in amount[other_half]:
            if letters == other_letters:
                repeated.append(other_letters)

print(repeated)



all_pairs = open("pairs.txt").read()
split_pairs = all_pairs.split("\n")
overlap_sum = 0

pair_list = []
sections = ""

for pairs in split_pairs:
    for elfs in pairs:
        if elfs == "-" or elfs == ",":
            pair_list.append(int(sections))
            sections = ""
            pass
        else:
            sections += elfs
    pair_list.append(int(sections))
    sections = ""
    if (pair_list[0] <= pair_list[2] and pair_list[1] >= pair_list[3]) or (pair_list[2] <= pair_list[0] and pair_list[3] >= pair_list[1]):
        overlap_sum += 1
    pair_list = []

print(overlap_sum)

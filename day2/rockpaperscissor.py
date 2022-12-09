placeholder = open("rcp.txt").read()
rcp = placeholder.split("\n")
print(rcp)

score = 0

# a = rock || x = 1
# b = paper || y = 2
# c = scissor || z = 3

# win = 6
# tie = 3
# lost = 0



for games in rcp:
    if games == "A X": # rock rock, 1 + tie 3
        score += 4
    elif games == "A Y": # rock paper, 2 + win 6
        score += 8
    elif games == "A Z": # rock scissor, 3 + loss 0
        score += 3
    elif games == "B X": # paper rock, 1 + 0 loss
        score += 1
    elif games == "B Y": # paper paper, 2 + tie 3
        score += 5
    elif games == "B Z": # paper scissor, 3 + win 6
        score += 9
    elif games == "C X": # scissor rock, 1 + win 6
        score += 7
    elif games == "C Y": # scissor paper, 2 + lost 0
        score += 2
    elif games == "C Z": # scissor scissor 3 + tie 3
        score += 6

print(score)

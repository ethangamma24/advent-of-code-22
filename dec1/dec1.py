curr_calories = 0
max_calories = 0

def partOne():
    input = open('input.txt', 'r')
    lines = input.readlines()
    global curr_calories
    global max_calories

    for line in lines:
        if line == '\n':
            max_calories = max(curr_calories, max_calories)
            curr_calories = 0
        else:
            curr_calories += int(line)

    print(max_calories)


def partTwo():
    input = open('input.txt', 'r')
    lines = input.readlines()
    global curr_calories
    top_three = [0, 0, 0]

    for line in lines:
        if line == '\n':
            compareTopThree(top_three)
            curr_calories = 0
        else:
            curr_calories += int(line)

    print(sum(top_three))

def compareTopThree(top_three):
    global curr_calories
    if curr_calories > min(top_three):
        top_three[top_three.index(min(top_three))] = curr_calories

#partOne()
partTwo()

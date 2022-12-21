legend_one = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
''' 
For lengend_two, I have adjusted the values to be the points
I will recieve for each corresponding outcome.
E.g.: The opponent plays paper (B), and I need to lose (X).
      I will play the losing value (A), which is one point less
      than what the opponent plays. My total score is then 1.
''' 
legend_two = {'A': 1, 'B': 2, 'C': 3, 'X': 0, 'Y': 3, 'Z': 6}
player_options = [1,2,3]
score = 0

def main():
    global score
    input = open('input.txt', 'r')
    lines = input.readlines()

    for line in lines:
        # score += calculateScorePartOne(line[0], line[2])
        score += calculateScorePartTwo(line[0], line[2])

    print(score)

def calculateScorePartOne(opp, player):
    global legend_one
    if legend[player] == legend[opp] + 1 or legend[player] == legend[opp] - 2:
        score = 6 + legend[player]
    elif legend[player] == legend[opp]:
        score = 3 + legend[player]
    else:
        score = legend[player]
    
    return score

# 
def calculateScorePartTwo(opp, outcome):
    global legend_two
    match outcome:
        case 'X':
            try:
                score = 0 + player_options[legend_two[opp] - 2]
            except Exception:
                score = 0 + 3
        case 'Y':
            score = 3 + legend_two[opp]
        case 'Z':
            try:
                score = 6 + player_options[legend_two[opp]]
            except Exception:
                score = 6 + 1
    return score

main()

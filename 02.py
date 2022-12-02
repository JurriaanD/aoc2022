SHAPE_SCORE_ROCK = 1
SHAPE_SCORE_PAPER = 2
SHAPE_SCORE_SCISSORS = 3
WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0

def part1():
    # A/X = Rock
    # B/Y = Paper
    # C/Z = Scissors

    round_score = {
        "A": {
            "X": SHAPE_SCORE_ROCK + DRAW_SCORE,
            "Y": SHAPE_SCORE_PAPER + WIN_SCORE,
            "Z": SHAPE_SCORE_SCISSORS + LOSS_SCORE,
        },
        "B": {
            "X": SHAPE_SCORE_ROCK + LOSS_SCORE,
            "Y": SHAPE_SCORE_PAPER + DRAW_SCORE,
            "Z": SHAPE_SCORE_SCISSORS + WIN_SCORE,
        },
        "C": {
            "X": SHAPE_SCORE_ROCK + WIN_SCORE,
            "Y": SHAPE_SCORE_PAPER + LOSS_SCORE,
            "Z": SHAPE_SCORE_SCISSORS + DRAW_SCORE,
        }
    }

    with open('02.in', 'r') as f:
        score = 0
        for line in f:
            opponent, me = line.strip().split(" ")
            score += round_score[opponent][me]
        return score

def part2():
    # A = Rock, B = Paper, C = Scissors
    # X = Lose, Y = Draw, Z = Win

    round_score = {
        "A": {
            "X": LOSS_SCORE + SHAPE_SCORE_SCISSORS,
            "Y": DRAW_SCORE + SHAPE_SCORE_ROCK,
            "Z": WIN_SCORE + SHAPE_SCORE_PAPER,
        },
        "B": {
            "X": LOSS_SCORE + SHAPE_SCORE_ROCK,
            "Y": DRAW_SCORE + SHAPE_SCORE_PAPER,
            "Z": WIN_SCORE + SHAPE_SCORE_SCISSORS,
        },
        "C": {
            "X": LOSS_SCORE + SHAPE_SCORE_PAPER,
            "Y": DRAW_SCORE + SHAPE_SCORE_SCISSORS,
            "Z": WIN_SCORE + SHAPE_SCORE_ROCK,
        }
    }

    with open('02.in', 'r') as f:
        score = 0
        for line in f:
            opponent, outcome = line.strip().split(" ")
            score += round_score[opponent][outcome]
        return score

if __name__ == "__main__":
    ans1 = part1()
    print(f"The answer for part 1 is {ans1}")
    ans2 = part2()
    print(f"And the answer for part 2 is {ans2}")
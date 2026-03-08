import sys


def score_cruncher(arguments: list[str]) -> None:
    int_list: list[int] = []
    for arg in arguments[1:]:
        try:
            score = int(arg)
            int_list.append(score)
        except ValueError:
            print(f"Skipping invalid score: {arg}")

    total = 0
    number_of_arguments = len(arguments) - 1
    highest_score = int_list[0]
    lowest_score = int_list[0]
    for i in int_list:
        total += i
        if i > highest_score:
            highest_score = i
        if i < lowest_score:
            lowest_score = i
    print(f"Scores processed: {int_list}")
    print(f"Total players: {number_of_arguments}")
    print(f"Total score: {total}")
    print(f"Average score: {total / number_of_arguments}")
    print(f"High score: {highest_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {highest_score - lowest_score}")


def test_scores() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No score provided. Usage: python3 ft_score_analytics.py"
              "<score1> <score2> ...")
    else:
        score_cruncher(sys.argv)


if __name__ == "__main__":
    test_scores()

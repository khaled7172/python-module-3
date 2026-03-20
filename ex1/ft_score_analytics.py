import sys


def score_cruncher(arguments: list[str]) -> None:
    int_list: list[int] = []
    for arg in arguments[1:]:
        try:
            score = int(arg)
            int_list.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not int_list:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    total = sum(int_list)
    count = len(int_list)
    highest_score = max(int_list)
    lowest_score = min(int_list)
    print(f"Scores processed: {int_list}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {total / count}")
    print(f"High score: {highest_score}")
    print(f"Low score: {lowest_score}")
    print(f"Score range: {highest_score - lowest_score}")


def test_scores() -> None:
    print("=== Player Score Analytics ===")
    score_cruncher(sys.argv)


if __name__ == "__main__":
    test_scores()

import random


def test_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    print()
    players = ['Alice', 'bob', 'Charlie', 'dylan',
               'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")
    all_capitalized = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {all_capitalized}")
    already_capitalized = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {already_capitalized}")
    print()
    score_dict = {p: random.randint(1, 1000) for p in all_capitalized}
    print(f"Score dict: {score_dict}")
    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")
    high_scores = {p: s for p, s in score_dict.items() if s > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    test_data_alchemist()

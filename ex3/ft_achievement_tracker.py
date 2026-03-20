import random


ACHIEVEMENTS = [
    'Crafting Genius', 'World Savior', 'Master Explorer',
    'Collector Supreme', 'Untouchable', 'Boss Slayer',
    'Strategist', 'Unstoppable', 'Speed Runner', 'Survivor',
    'Treasure Hunter', 'First Steps', 'Sharp Mind',
    'Hidden Path Finder'
]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def test_achievements() -> None:
    print("=== Achievement Tracker System ===")
    print()
    players: dict[str, set[str]] = {
        'Alice': gen_player_achievements(),
        'Bob': gen_player_achievements(),
        'Charlie': gen_player_achievements(),
        'Dylan': gen_player_achievements(),
    }
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()
    all_achievements: set[str] = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}")
    common = all_achievements.copy()
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")
    print()
    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = others.union(other_ach)
        unique = achievements.difference(others)
        print(f"Only {name} has: {unique}")
    print()
    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    test_achievements()

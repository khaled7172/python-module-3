def test_game_analytics() -> None:
    players: list[str] = ["alice", "bob", "charlie", "diana"]

    scores: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2050
    }

    achievements: dict[str, list[str]] = {
        "alice": ["first_kill", "level_10", "boss_slayer"],
        "bob": ["first_kill"],
        "charlie": ["first_kill", "level_10", "boss_slayer", "arena_win"],
        "diana": ["first_kill", "arena_win"]
    }
    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")
    high_score = [p for p in scores if scores[p] > 2000]
    print(f"High scorers (>2000): {high_score}")
    doubled_scores = [scores[p] * 2 for p in scores]
    print(f"Scores doubled: {doubled_scores}")
    active_players = [p for p in players if p != "diana"]
    print(f"Active players: {active_players}")
    print()
    print("=== Dict Comprehension Examples ===")
    player_scores = {p: scores[p] for p in players}
    print(f"Player scores: {player_scores}")
    achievemens_counts = {p: len(achievements[p]) for p in players}
    score_catgories = {
        player: "high" if score > 2000 else "medium" for player,
        score in scores.items()}
    print(f"Score categories: {score_catgories}")
    print(f"Achievement counts: {achievemens_counts}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_players = {p for p in players}
    print(f"Unique players: {unique_players}")
    unique_achievements = {
        achievement
        for player in achievements
        for achievement in achievements[player]
    }
    print(f"Unique achievements: {unique_achievements}")
    regions = ["north", "east", "north", "central"]
    active_regions = {region for region in regions}
    print(f"Active regions: {active_regions}")
    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {sum(scores.values()) / len(scores)}")
    print(f"Top performer: {max(scores, key=scores.get)}")


if __name__ == "__main__":
    test_game_analytics()

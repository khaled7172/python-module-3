def test_achievements():
    print("=== Achievement Tracker System ===")
    print()
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {
        'level_10',
        'treasure_hunter',
        'speed_demon',
        'boss_slayer',
        'perfectionist'}
    players = {
        'Alice': alice,
        'Bob': bob,
        'Charlie': charlie
    }
    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")
    print()
    print("=== Achievement Analytics ===")
    all_unique_items = bob | alice | charlie
    rare_achievement = set()
    for ach in all_unique_items:
        count = 0
        if ach in alice:
            count += 1
        if ach in bob:
            count += 1
        if ach in charlie:
            count += 1
        if count == 1:
            rare_achievement.add(ach)
    length_unique = len(all_unique_items)
    common_achievement = bob & alice & charlie
    print(f"All unique achievements: {all_unique_items}")
    print(f"Total unique achievements: {length_unique}")
    print()
    print(f"Common to all players: {common_achievement}")
    print(f"Rare achievements (1 player): {rare_achievement}")
    print()
    alice_bob_common = alice & bob
    alice_unique = alice - bob
    bob_unique = bob - alice
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    test_achievements()

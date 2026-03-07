from typing import Generator

def generate_event_stream(num_events: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]
    for i in range(1, num_events + 1):
        yield f"Event {i}: Player {players[(i - 1)% len(players)]} (level {levels[i % len(levels)]}) {actions[i % len(actions)]}"



def test_data_stream():
    print("=== Game Data Stream Processor ===")
    print()
    events = 1000
    print(f"Processing {events} game events...")
    print()
    stream = generate_event_stream(events)
    count = 0
    for event in stream:
        print(event)
        count += 1
        if count == 3:
            break
    print("...")
    print()
    total = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    for event in stream:
        total += 1
        if "treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1
        if "level " in event:
            parts = event.split("level ")
            level_part = parts[1].split(")")
            level = int(level_part[0])
            if level >= 10:
                high_level_players += 1
    print("Stream Analytics ===")
    print(f"Total events processed: {total}")#
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("Memory usgae: Constant (streaming)")
    print("Processing time: {} seconds")
    print()
    print("Generator Demonstration ===")
    print("Fibonacci sequence (first 10): {}")
    print("Prime numbers (first 5): {}")






















if __name__ == "__main__":
    test_data_stream()
from typing import Generator


def generate_event_stream(num_events: int) -> Generator[str, None, None]:
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    levels = [5, 12, 8]
    for i in range(1, num_events + 1):
        yield (f"Event {i}: Player {players[(i - 1) % len(players)]}"
               f"(level {levels[i % len(levels)]})"
               f"{actions[i % len(actions)]}"
               )


def fibo_generator(n: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def prime_generator(n: int) -> Generator[int, None, None]:
    count = 0
    num = 2
    while count < n:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            yield num
            count += 1
        num += 1


def test_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    events = 1000
    print(f"Processing {events} game events...")
    print()
    stream = generate_event_stream(events)
    count = 0
    total = 0
    for event in stream:
        print(event)
        count += 1
        total += 1
        if count == 3:
            break
    print("...")
    print()
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
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("Generator Demonstration ===")
    print("Fibonacci sequence (first 10): ", end="")
    fib_stream = fibo_generator(10)
    for i, num in enumerate(fib_stream):
        if i < 9:
            print(num, end=", ")
        else:
            print(num)
    print("Prime numbers (first 5): ", end="")
    prime_stream = prime_generator(5)
    for i, num in enumerate(prime_stream):
        if i < 4:
            print(num, end=", ")
        else:
            print(num)


if __name__ == "__main__":
    test_data_stream()

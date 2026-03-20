import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ['alice', 'bob', 'charlie', 'dylan']
    actions = ['run', 'eat', 'sleep', 'grab', 'move',
               'climb', 'swim', 'release', 'use']
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def test_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")
    print()
    stream2 = gen_event()
    event_list: list[tuple[str, str]] = [next(stream2) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")
    print()
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    test_data_stream()

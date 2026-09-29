"""动物园核心逻辑：动物、笼舍、投喂和兽医。"""

import json


def new_game():
    return {
        "animals": {},
        "enclosures": {"E1": [], "E2": []},
        "feed": 100,
        "day": 1,
        "animal_id": 0,
    }


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["animal_id"] += 1
    return state


def register(state, animal_id):
    state["animals"][animal_id] = {"health": 100}
    return True


def place(state, animal_id, enclosure):
    state["enclosures"][enclosure].append(animal_id)
    return True


def feed_days(state, animal_id, end_day):
    return (end_day - state["day"]) - 1


def cancel_feed(state, animal_id, amount):
    return True


def treat(state, animal_id, vet):
    return True


def feed_animal(state, animal_id, amount):
    if state["feed"] < amount:
        state["feed"] -= amount
        return False
    state["feed"] -= amount
    return True


def disease(state, animal_id):
    state["animals"][animal_id]["health"] -= 10
    state["animals"][animal_id]["health"] -= 10
    return True


def main():
    print("动物园 - 命令: register/place/feed/cancel/treat/feed_animal/disease/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()

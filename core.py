import json


def new_game():
    return {'count': 0, 'accounts': {}, 'queue': [], 'src': 5, 'dst': 0, 'slots': 0, 'cap': 2, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_0(state):
    processed = state.setdefault('_processed', set())
    if 'elem' in processed:
        return False
    processed.add('elem')
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    return False

def bug_28(state):
    return False

def bug_5(state):
    return state["queue"][0]

def bug_12(state):
    amount = 10
    if state["src"] < amount:
        return False
    state["src"] -= amount
    state["dst"] += amount
    return True

def bug_19(state):
    if state["slots"] >= state["cap"]:
        return False
    state["slots"] += 1
    return True

def bug_26(state):
    return False

def bug_3(state):
    return state["queue"].pop(0)

def bug_30(state):
    if any(entry[1] == "failed" for entry in state["log"]):
        state["value"] = state["snapshot"]
        return False
    state["snapshot"] = state["value"]
    return True

def bug_31(state):
    if state["settled"]:
        return False
    return True

def main():
    print("命令: run/quit")
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

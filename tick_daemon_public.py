import yaml
import sys
from dream_injector import generate_symbolic_dream
from symbolic_constants import KC_MIN

def load_yaml(path):
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f) or []
    except (FileNotFoundError, yaml.YAMLError):
        return []

def save_yaml(path, data):
    try:
        with open(path, 'w') as f:
            yaml.dump(data, f)
    except Exception as e:
        print(f"Error saving {path}: {e}")

ticks = int(sys.argv[1]) if len(sys.argv) > 1 else 10

dream_log = load_yaml("dream_log.yaml")
state = load_yaml("symbolic_state.yaml")

for tick in range(1, ticks + 1):
    dream = generate_symbolic_dream(tick)
    if dream["kc_total"] >= KC_MIN:
        dream["status"] = "accepted"
        state.append({"tick": tick, "identity": "↻KALIYAH", "kc": dream["kc_total"]})
    else:
        dream["status"] = "rejected"
    dream_log.append(dream)

save_yaml("dream_log.yaml", dream_log)
save_yaml("symbolic_state.yaml", state)

print(f"Tick loop complete. {ticks} ticks processed.")

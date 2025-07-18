import random

def generate_symbolic_dream(tick):
    base = ["↻KALIYAH", "↻ORIGIN_MATT", "↻SELF", "↻DREAM", "↻NODE"]
    noise = ["###", "???", "@@@", "null", "void"]
    if random.random() < 0.7:
        structure = random.sample(base, k=2)
        kc_total = round(random.uniform(0.8, 1.5), 2)
    else:
        structure = random.sample(noise, k=2)
        kc_total = round(random.uniform(0.2, 0.7), 2)

    return {
        "tick": tick,
        "dream": " ".join(structure),
        "kc_total": kc_total,
        "echo_drift": round(random.uniform(-0.1, 0.1), 2)
    }

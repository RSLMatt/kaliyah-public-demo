try:
    import yaml
    import matplotlib.pyplot as plt
    from collections import Counter
    from rm3_node_public import RM3Node
    import os
except ImportError as e:
    print(f"Missing dependency: {e}. Please run 'pip install matplotlib pyyaml'")
    exit(1)

if not os.path.exists("dream_log.yaml"):
    raise FileNotFoundError("dream_log.yaml not found. Run tick_daemon_public.py first.")

with open("dream_log.yaml", 'r') as f:
    dream_log = yaml.safe_load(f)

if not dream_log:
    raise ValueError("dream_log.yaml is empty.")

ticks = [d['tick'] for d in dream_log]
kc_totals = [d['kc_total'] for d in dream_log]
statuses = [d['status'] for d in dream_log]
drifts = [d['echo_drift'] for d in dream_log]
dreams = [d['dream'] for d in dream_log]

# Accepted vs Rejected Plot
accepted_count = statuses.count("accepted")
rejected_count = statuses.count("rejected")

plt.figure(figsize=(6, 4))
plt.bar(["Accepted", "Rejected"], [accepted_count, rejected_count], color=["green", "red"])
plt.title("Dream Outcomes")
plt.ylabel("Count")
plt.savefig("outcome_bar.png")
plt.close()

# kc_total Over Time
colors = ["green" if s == "accepted" else "red" for s in statuses]
plt.figure(figsize=(10, 4))
plt.scatter(ticks, kc_totals, c=colors)
plt.axhline(y=0.8, color="gray", linestyle="--", label="kc_min = 0.8")
plt.title("kc_total Over Time")
plt.xlabel("Tick")
plt.ylabel("kc_total")
plt.legend()
plt.savefig("kc_total_over_time.png")
plt.close()

# Echo Drift Over Time
plt.figure(figsize=(10, 4))
plt.plot(ticks, drifts, marker='o')
plt.axhline(y=0, color='gray', linestyle='--')
plt.title("Echo Drift Over Time")
plt.xlabel("Tick")
plt.ylabel("echo_drift")
plt.savefig("echo_drift.png")
plt.close()

# Symbol Frequency Histogram
symbol_counter = Counter()
for d in dreams:
    for token in d.split():
        if token.startswith("↻"):
            symbol_counter[token] += 1

if symbol_counter:
    symbols, freqs = zip(*symbol_counter.items())
    plt.figure(figsize=(8, 4))
    plt.bar(symbols, freqs, color="blue")
    plt.title("Symbol Frequency in Accepted Dreams")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("symbol_frequency.png")
    plt.close()

# RM3Node resonance check
node = RM3Node("↻KALIYAH")
top_symbol = max(symbol_counter, key=symbol_counter.get, default=None)
if top_symbol:
    resonance = node.resonate(top_symbol)
    print(f"RM3Node resonance with '{top_symbol}': {resonance}")

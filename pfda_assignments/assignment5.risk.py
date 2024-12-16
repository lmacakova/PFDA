# Importing modules
import random
import matplotlib.pyplot as plt
import numpy as np

# Function to simulate a single battle round
def simulate_battle_round():
    attacker_rolls = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)
    defender_rolls = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)

    attacker_losses = 0
    defender_losses = 0

    # Compare dice rolls
    for attacker_die, defender_die in zip(attacker_rolls, defender_rolls):
        if attacker_die > defender_die:
            defender_losses += 1
        else:
            attacker_losses += 1

    return attacker_losses, defender_losses

# Simulate 1000 battle rounds
def simulate_1000_battle_rounds():
    results = []
    for _ in range(1000):
        results.append(simulate_battle_round())

    attacker_losses = [result[0] for result in results]
    defender_losses = [result[1] for result in results]

    # Plot results
    labels = ['0 Losses', '1 Loss', '2 Losses']
    attacker_counts = [attacker_losses.count(i) for i in range(3)]
    defender_counts = [defender_losses.count(i) for i in range(3)]

    x = np.arange(len(labels))  # Label locations
    width = 0.35  # Bar width

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, attacker_counts, width, label='Attacker Losses')
    ax.bar(x + width / 2, defender_counts, width, label='Defender Losses')

    ax.set_xlabel('Number of Losses in a Round')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Losses in 1000 Risk Battle Rounds')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

# Simulate full battle between armies until one side is wiped out
def simulate_full_battle(attacker_troops, defender_troops):
    attacker_losses_history = []
    defender_losses_history = []

    while attacker_troops > 0 and defender_troops > 0:
        attacker_rolls = min(attacker_troops, 3)
        defender_rolls = min(defender_troops, 2)

        attacker_losses, defender_losses = simulate_battle_round()

        # Update troop counts
        attacker_troops -= min(attacker_rolls, attacker_losses)
        defender_troops -= min(defender_rolls, defender_losses)

        # Record losses
        attacker_losses_history.append(attacker_troops)
        defender_losses_history.append(defender_troops)

    return attacker_losses_history, defender_losses_history

# Visualize full battle results
def visualize_full_battle(attacker_troops, defender_troops):
    attacker_history, defender_history = simulate_full_battle(attacker_troops, defender_troops)

    plt.figure(figsize=(10, 6))
    plt.plot(attacker_history, label='Attacker Troops', color='red')
    plt.plot(defender_history, label='Defender Troops', color='blue')
    plt.xlabel('Battle Rounds')
    plt.ylabel('Remaining Troops')
    plt.title('Troop Levels During Full Battle')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("Simulating 1000 individual battle rounds...")
    simulate_1000_battle_rounds()

    print("Simulating a full battle...")
    visualize_full_battle(attacker_troops=50, defender_troops=30)

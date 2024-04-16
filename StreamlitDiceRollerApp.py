import streamlit as st
import random

def roll_dice(dice_configurations):
    """Roll specified configurations of dice and return individual rolls and results by type."""
    rolls = []
    results = {}
    for num_dice, sides_per_die in dice_configurations:
        dice_rolls = [random.randint(1, sides_per_die) for _ in range(num_dice)]
        rolls.extend(dice_rolls)
        results[f"{num_dice}d{sides_per_die}"] = dice_rolls
    return rolls, results

def main():
    st.title("Interactive Dice Roller Simulator")
    
    # Dictionary to hold the count of each dice type
    dice_counts = {'d4': 0, 'd6': 0, 'd8': 0, 'd10': 0, 'd12': 0, 'd20': 0, 'd100': 0}

    # Display dice buttons and track counts
    col1, col2, col3 = st.columns(3)
    dice_keys = list(dice_counts.keys())
    for i, key in enumerate(dice_keys):
        with (col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3):
            if st.button(f"Add {key}"):
                dice_counts[key] += 1

    # Display current dice configuration
    st.write("Current dice selection:")
    selected_config = ' '.join(f"{count}{die}" for die, count in dice_counts.items() if count > 0)
    st.write(selected_config)

    modifier = st.number_input("Enter the modifier to apply to the total roll (can be negative):", value=0)

    # Button to roll dice
    if st.button("Roll Dice") and any(dice_counts.values()):
        dice_configurations = [(count, int(die[1:])) for die, count in dice_counts.items() if count > 0]
        rolls, results = roll_dice(dice_configurations)
        roll_total = sum(rolls) + modifier

        # Display the results
        for key, value in results.items():
            st.write(f"**{key} rolls:** {', '.join(map(str, value))}")
        st.write(f"**Total before modifier:** {sum(rolls)}")
        st.write(f"**Modifier:** {modifier}")
        st.write(f"**Final Result:** {roll_total}")

if __name__ == "__main__":
    main()

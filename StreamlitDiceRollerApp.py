import streamlit as st
import random

def roll_dice(dice_configurations, total_modifier):
    """Roll specified configurations of dice and return individual rolls and total with modifiers."""
    rolls = [random.randint(1, sides_per_die) for num_dice, sides_per_die in dice_configurations for _ in range(num_dice)]
    roll_total = sum(rolls) + total_modifier
    return rolls, roll_total

def main():
    st.title("Interactive Dice Roller Simulator with Modifiers")

    # Modifier input section
    st.sidebar.title("Configure Modifiers")
    modifiers = {
        "Competencia": st.sidebar.number_input("Competencia", min_value=0, value=0),
        "Fuerza": st.sidebar.number_input("Fuerza", min_value=0, value=0),
        "Destreza": st.sidebar.number_input("Destreza", min_value=0, value=0),
        "Constitución": st.sidebar.number_input("Constitución", min_value=0, value=0),
        "Inteligencia": st.sidebar.number_input("Inteligencia", min_value=0, value=0),
        "Sabiduría": st.sidebar.number_input("Sabiduría", min_value=0, value=0),
        "Carisma": st.sidebar.number_input("Carisma", min_value=0, value=0),
        "Magia": st.sidebar.number_input("Magia", min_value=0, value=0),
    }

    # Display dice buttons and track counts
    dice_counts = {f"d{num}": 0 for num in [4, 6, 8, 10, 12, 20, 100]}
    cols = st.columns(3)
    for i, (dice, count) in enumerate(dice_counts.items()):
        with cols[i % 3]:
            if st.button(f"Add {dice}"):
                dice_counts[dice] += 1

    # Display current dice configuration
    st.write("Current dice selection:")
    selected_config = ' '.join(f"{count}{dice}" for dice, count in dice_counts.items() if count > 0)
    st.write(selected_config)

    # Select modifiers
    st.write("Select Modifiers:")
    selected_modifiers = {mod: st.checkbox(mod, value=False) for mod in modifiers}
    total_modifier = sum(modifiers[mod] for mod, selected in selected_modifiers.items() if selected)

    # Button to roll dice
    if st.button("Roll Dice"):
        dice_configurations = [(count, int(dice[1:])) for dice, count in dice_counts.items() if count > 0]
        rolls, roll_total = roll_dice(dice_configurations, total_modifier)

        # Display the results
        st.write(f"Rolls: {rolls}")
        st.write(f"Total before modifier: {sum(rolls)}")
        st.write(f"Total modifiers applied: {total_modifier}")
        st.write(f"Final Total: {roll_total}")

if __name__ == "__main__":
    main()

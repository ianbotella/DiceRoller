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
    st.title("Advanced Dice Roller Simulator")

    # Dynamic addition of dice configurations using a form
    with st.form("dice_form"):
        dice_config_inputs = st.text_input("Enter dice configurations (e.g., 2d6 1d8):")
        modifier = st.number_input("Enter the modifier to apply to the total roll (can be negative):", value=0)
        submit_button = st.form_submit_button("Roll Dice")

    if submit_button and dice_config_inputs:
        try:
            # Parse the input configurations
            dice_configurations = []
            parts = dice_config_inputs.split()
            for part in parts:
                num_dice, dice_type = part.split('d')
                dice_configurations.append((int(num_dice), int(dice_type)))

            rolls, results = roll_dice(dice_configurations)
            roll_total = sum(rolls) + modifier

            # Display the results
            for key, value in results.items():
                st.write(f"**{key} rolls:** {', '.join(map(str, value))}")
            st.write(f"**Total before modifier:** {sum(rolls)}")
            st.write(f"**Modifier:** {modifier}")
            st.write(f"**Final Result:** {roll_total}")
        except ValueError:
            st.error("Invalid dice configuration format. Please enter in the format 'NdM' (e.g., 2d6 1d8).")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()

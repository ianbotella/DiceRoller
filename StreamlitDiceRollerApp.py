import streamlit as st
import random

def roll_dice(ndice_configurations):
  rolls = []
  results = {}
  for config in dice_configurations:
    num_dice, sides_per_die = config
    dice_rolls = [random.randint(1, sides_per_die) for _ in range(num_dice)]
    rolls.extend(dice_rolls)
    results[f"{num_dice}d{sides_per_die}"] = dice_rolls
  return rolls, results

def main():
  st.title("Dice Roller Simulator")

  with st.form("dice_form"):
    dice_config_inputs = st.text_input("Enter dice configurations (e.g. 2d6 1d8):")
    modifier = st.number_input("Enter the modifier to apply to the total roll (can be negative):", value=0)
    submit_button = st.form_submit_button("Roll Dice")

  if submit_button and dice_config_inputs:
    dice_configurations = []
    try:
      parts = dice_config_inputs.split()
      for part in parts:
        num_dice, dice_type = part.split('d')
        dice_configurations.append((int(num_dice), int(dice_type)))

      rolls, results = roll_dice(dice_configurations)
      roll_total = sum(rolls) + modifier

      for key, value in results.items():
        st.write(f"**{key} rolls:** {', '.join(map(str, value))}")
      st.write(f"**Total before modifier:** {sum(rolls)}")
      st.write(f"**Modifier:** {modifier}")
      st.write(f"**Final Result:** {roll_total}")
    except Exception as e:
      st.error(f"Error parsing dice configurations: {str(e)}")

if __name__ == "__main__":
  main()

import streamlit as st
import random

def roll_dice(num_dice, sides_per_die):
  return [random.randint(1, sides_per_die) for _ in range(num_dice)]

def main():
  st.title("Dice Roller Simulator")
  
  num_dice = st.number_input("Enter the number of dice to roll:", min_value=1, value=1)
  
  dice_options = {
    'd4': 4,
    'd6': 6,
    'd8': 8,
    'd10': 10,
    'd12': 12,
    'd20': 20,
    'd100': 100
  }
  selected_die = st.selectbox("Select the type of die:", list(dice_options.keys()), format_func=lambda x: f"{x} ({dice_options[x]} sides)")
  sides_per_die = dice_options[selected_die]
  
  modifier = st.number_input("Enter the modifier to apply to the total roll (can be negative):", value=0)
  
  if st.button("Roll Dice"):
    rolls = roll_dice(num_dice, sides_per_die)
    roll_total = sum(rolls) + modifier
    st.write("Results of individual rolls:")
    for index, roll in enumerate(rolls, start=1):
      st.write(f"Die {index}: {roll}")
    st.write(f"**Total before modifier:** {sum(rolls)}")
    st.write(f"**Modifier:** {modifier}")
    st.write(f"**Final Result:** {roll_total}")

if __name__ == "__main__":
  main()

import streamlit as st
import random

def roll_dice(num_dice, sides_per_die):
  return sum(random.randint(1, sides_per_die) for _ in range(num_dice))

def main():
  st.title("Dice Roller Simulator")
  num_dice = st.number_input("Enter the number of dice to roll:", min_value=1, value=1)
  sides_per_die = st.number_input("Enter the number of sides per die:", min_value=2, value=4)
  modifier = st.number_input("Enter the modifier to apply to the total roll (can be negative):", value=0)
  
  if st.button("Roll Dice"):
    roll_total = roll_dice(num_dice, sides_per_die)
    final_result = roll_total + modifier
    st.write(f"**Roll Total:** {roll_total}")
    st.write(f"**Modifier:** {modifier}")
    st.write(f"**Final Result:** {final_result}")

if __name__ == "__main__":
  main()

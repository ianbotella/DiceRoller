import streamlit as st
import random

# CSS to customize button appearances
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&display=swap');

html, body, [class*="css-"] {
    font-family: 'Libre Baskerville', serif;
}
button, .stButton>button {
    color: white;
    font-size: 16px;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    font-family: 'Libre Baskerville', serif; /* Ensure buttons also use the font */
}
button:hover, .stButton>button:hover {
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

def calculate_modifier(value):
    if value <= 1:
        return -5
    elif 2 <= value <= 3:
        return -4
    elif 4 <= value <= 5:
        return -3
    elif 6 <= value <= 7:
        return -2
    elif 8 <= value <= 9:
        return -1
    elif 10 <= value <= 11:
        return 0
    elif 12 <= value <= 13:
        return 1
    elif 14 <= value <= 15:
        return 2
    elif 16 <= value <= 17:
        return 3
    elif 18 <= value <= 19:
        return 4
    elif 20 <= value <= 21:
        return 5
    elif 22 <= value <= 23:
        return 6
    elif 24 <= value <= 25:
        return 7
    elif 26 <= value <= 27:
        return 8
    elif 28 <= value <= 29:
        return 9
    elif value >= 30:
        return 10
    else:
        return 0  # Considerar un valor por defecto para entradas inválidas o fuera de rango


def roll_dice(dice_configurations):
    """Roll specified configurations of dice and return individual rolls and results by type."""
    rolls = []
    results = {}
    for num_dice, sides_per_die in dice_configurations:
        dice_rolls = [random.randint(1, sides_per_die) for _ in range(num_dice)]
        rolls.extend(dice_rolls)
        results[f"{num_dice}d{sides_per_die}"] = dice_rolls
    return rolls, results

def reset_dice_counts():
    """Reset the dice counts to zero."""
    for key in st.session_state.dice_counts.keys():
        st.session_state.dice_counts[key] = 0

def main():
    st.title("Interactive Dice Roller Simulator")

    # Crear campos de entrada para modificadores y mostrar los resultados calculados
    st.sidebar.title("Ingrese valores para Modificadores")
    abilities = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma", "Magia", "Competencia"]
    modifiers = {}
    for ability in abilities:
        value = st.sidebar.number_input(f"Valor de {ability}", min_value=1, max_value=30, value=10)
        modifier = calculate_modifier(value)
        modifiers[ability] = modifier
        st.sidebar.write(f"Modificador de {ability}: {modifier}")
    
    # Initialize session state for dice counts if not already done
    if 'dice_counts' not in st.session_state:
        st.session_state.dice_counts = {'d4': 0, 'd6': 0, 'd8': 0, 'd10': 0, 'd12': 0, 'd20': 0, 'd100': 0}

    # Display dice buttons and track counts
    cols = st.columns(3)
    dice_keys = list(st.session_state.dice_counts.keys())
    for i, key in enumerate(dice_keys):
        with cols[i % 3]:
            if st.button(f"{key}"):
                st.session_state.dice_counts[key] += 1

    # Display current dice configuration
    st.write("Current dice selection:")
    selected_config = ' '.join(f"{count}{die}" for die, count in st.session_state.dice_counts.items() if count > 0)
    st.write(selected_config)

    modifier = st.number_input("Enter the modifier to apply to the total roll (can be negative):", value=0)

    # Button to roll dice
    if st.button("Roll Dice") and any(st.session_state.dice_counts.values()):
        dice_configurations = [(count, int(die[1:])) for die, count in st.session_state.dice_counts.items() if count > 0]
        rolls, results = roll_dice(dice_configurations)
        roll_total = sum(rolls) + modifier

        # Display the results
        for key, value in results.items():
            st.write(f"**{key} rolls:** {', '.join(map(str, value))}")
        st.write(f"**Total before modifier:** {sum(rolls)}")
        st.write(f"**Modifier:** {modifier}")
        st.write(f"**Final Result:** {roll_total}")

        # Optionally reset the dice counts after rolling
        reset_dice_counts()

    # Button to manually reset dice selection
    if st.button("Reset Dice"):
        reset_dice_counts()

if __name__ == "__main__":
    main()

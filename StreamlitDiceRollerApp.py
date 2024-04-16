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
    # Tus reglas de conversión aquí
    return ...

def roll_dice(dice_configurations, total_modifier):
    rolls = []
    results = {}
    for num_dice, sides_per_die in dice_configurations:
        dice_rolls = [random.randint(1, sides_per_die) for _ in range(num_dice)]
        rolls.extend(dice_rolls)
        results[f"{num_dice}d{sides_per_die}"] = dice_rolls
    roll_total = sum(rolls) + total_modifier
    return rolls, results

def main():
    st.title("Interactive Dice Roller Simulator")
    st.sidebar.title("Configure Modifiers")

    # Define abilities and get input for modifiers
    abilities = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma", "Magia", "Competencia"]
    modifiers = {ability: st.sidebar.number_input(f"Valor de {ability}", min_value=1, max_value=30, value=10, step=1) for ability in abilities}
    
    # Calculate modifiers based on values entered
    calculated_modifiers = {ability: calculate_modifier(value) for ability, value in modifiers.items()}
    
    # Choose ability to apply additional modifier
    selected_ability = st.selectbox("Seleccione la habilidad para aplicar al lanzamiento:", options=abilities)
    additional_modifier = calculated_modifiers[selected_ability]
    st.write(f"Modificador adicional seleccionado: {additional_modifier}")

    # Dice configuration
    dice_counts = {f"d{num}": 0 for num in [4, 6, 8, 10, 12, 20, 100]}
    cols = st.columns(3)
    for i, key in enumerate(dice_counts):
        with cols[i % 3]:
            if st.button(f"Añadir {key}"):
                st.session_state.dice_counts[key] += 1

    selected_config = ' '.join(f"{count}{die}" for die, count in st.session_state.dice_counts.items() if count > 0)
    st.write("Configuración de dados seleccionada:", selected_config)

    if st.button("Lanzar Dados"):
        dice_configurations = [(count, int(die[1:])) for die, count in st.session_state.dice_counts.items() if count > 0]
        rolls, roll_total = roll_dice(dice_configurations, additional_modifier)
        st.write(f"Resultados individuales de los dados: {rolls}")
        st.write(f"Total antes del modificador: {sum(rolls)}")
        st.write(f"Modificador aplicado: {additional_modifier}")
        st.write(f"Total Final: {roll_total}")
        reset_dice_counts()

    if st.button("Resetear Selección de Dados"):
        reset_dice_counts()

def reset_dice_counts():
    for key in st.session_state.dice_counts.keys():
        st.session_state.dice_counts[key] = 0

if __name__ == "__main__":
    main()

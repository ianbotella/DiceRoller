import streamlit as st
import random

def calcular_modificador(value):
    return (value - 10) // 2

def roll_dice(dice_type, count):
    return [random.randint(1, dice_type) for _ in range(count)]

def setup_session_state():
    if 'dice_counts' not in st.session_state:
        st.session_state.dice_counts = {f"d{num}": 0 for num in [4, 6, 8, 10, 12, 20, 100]}
        st.session_state.results = {}

def main():
    st.title("Dice Roller")
    setup_session_state()

    dice_types = [4, 6, 8, 10, 12, 20, 100]
    st.subheader("Seleccione los dados para lanzar:")
    cols = st.columns(len(dice_types))

    for idx, dice in enumerate(dice_types):
        with cols[idx]:
            if st.button(f"1d{dice}"):
                st.session_state.dice_counts[f"d{dice}"] += 1
                st.experimental_rerun()

    display_selected_dice()
    handle_abilities_and_modifiers()
    roll_and_display_results()

def display_selected_dice():
    if any(st.session_state.dice_counts.values()):
        st.write("Dados seleccionados:")
        for dice, count in st.session_state.dice_counts.items():
            if count > 0:
                st.write(f"{count}{dice}")

def handle_abilities_and_modifiers():
    abilities = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma", "Magia", "Competencia"]
    abilities_values = {}
    abilities_modifier = {}

    for ability in abilities:
        value = st.sidebar.number_input(f"**{ability}**", min_value=1, max_value=30, value=10, step=1)
        abilities_values[ability] = value
        abilities_modifier[ability] = calcular_modificador(value) if ability not in ["Magia", "Competencia"] else value
        st.sidebar.write(f"Modificador: {abilities_modifier[ability]}")

def roll_and_display_results():
    selected_attributes = st.multiselect("Seleccione los atributos cuyos modificadores desea utilizar:",options = abilities + ["Sin Modificador"])
    if st.button("Lanzar Dados"):
        dice_results, total_dice = [], 0
        for dice, count in st.session_state.dice_counts.items():
            if count > 0:
                results = roll_dice(int(dice[1:]), count)
                dice_results.extend(results)
                st.session_state.results[dice] = results
                st.write(f"Resultados para {dice}: {results}")

        total_modifier = sum(abilities_modifier.get(attr, 0) for attr in selected_attributes if attr != "Sin Modificador")
        #total_dice = sum(dice_results)
        total = total_dice + total_modifier
        st.subheader("Resultados de la tirada:")
        #for dice, results in st.session_state.results.items():
        #    st.write(f"Resultados para {dice}: {results}")
        st.write(f"Total de dados: {total_dice}")
        st.write(f"Modificadores aplicados: {total_modifier}")
        st.write(f"Total: {total}")

        st.session_state.dice_counts = {key: 0 for key in st.session_state.dice_counts}

if __name__ == "__main__":
    main()

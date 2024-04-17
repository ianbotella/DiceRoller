import streamlit as st
import random

def calcular_modificador(value):
    # Implementa las reglas de conversión aquí
    if value <= 1:
        return -5
    elif value <= 3:
        return -4
    elif value <= 5:
        return -3
    elif value <= 7:
        return -2
    elif value <= 9:
        return -1
    elif value <= 11:
        return 0
    elif value <= 13:
        return 1
    elif value <= 15:
        return 2
    elif value <= 17:
        return 3
    elif value <= 19:
        return 4
    elif value <= 21:
        return 5
    elif value <= 23:
        return 6
    elif value <= 25:
        return 7
    elif value <= 27:
        return 8
    elif value <= 29:
        return 9
    else:
        return 10

def main():
    st.title("Interactive Dice Roller Simulator")

    # Define abilities and get input for modifiers
    abilities = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma", "Magia", "Competencia"]
    abilities_values = {}
    abilities_modifier = {}

    for ability in abilities:
        value = st.sidebar.number_input(f"**{ability}**", min_value=1, max_value=30, value=10, step=1)
        modifier = calcular_modificador(value)
        abilities_values[ability] = value
        abilities_modifier[ability] = modifier
        st.sidebar.write(f"Modificador: {modifier}")

    # Adding 'Sin Modificador' option to the multiselect
    options = abilities + ["Sin Modificador"]
    selected_attributes = st.multiselect("Seleccione los atributos cuyos modificadores desea utilizar:", options=abilities)

    # Calculate and display selected modifiers
    if selected_attributes:
        selected_modifiers = {attr: calcular_modificador(abilities_values[attr]) for attr in selected_attributes}
        st.write("Modificadores seleccionados:")
        for attr, mod in selected_modifiers.items():
            st.write(f"{attr}: {mod}")
    else:
        st.write("No se han seleccionado atributos.")

if __name__ == "__main__":
    main()

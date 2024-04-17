import streamlit as st

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

    # Inicializacion de contadores de dados en el estado de la sesion si no existen
    if 'dice_counts' not in st.session_state:
        st.session_state.dice_counts = {f"d{num}": 0 for num in [4, 6, 8, 10, 12, 20, 100]}

    dice_types = [4, 6, 8, 10, 12, 20, 100]
    st.write("Seleccione los dados para lanzar:")
    cols = st.columns(len(dice_types)) # Crea una columna para cada tipo de dado

    for idx, dice in enumerate(dice_types):
        label = f"d{dice}"
        with cols[idx]:
            if st.button(f"d{dice}"):
                st.session_state.dice_counts[label] += 1 # Incrementa el contador para el tipo de dado

    # Mostrar cuantos de cada tipo de dado han sido seleccionados
    if any(st.session_sate.dice_counts.values()):
        st.write("Dados seleccionados:")
        for dice, count in st.session_state.dice_counts.items():
            if count > 0:
                st.write(f"{count}d{dice}")

    # Define abilities and get input for modifiers
    abilities = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma", "Magia", "Competencia"]
    abilities_values = {}
    abilities_modifier = {}

    for ability in abilities:
        value = st.sidebar.number_input(f"**{ability}**", min_value=1, max_value=30, value=10, step=1)
        if ability in ["Magia", "Competencia"]:
            modifier = value
        else:
            modifier = calcular_modificador(value)
        abilities_values[ability] = value
        abilities_modifier[ability] = modifier
        st.sidebar.write(f"Modificador: {modifier}")

    # Adding 'Sin Modificador' option to the multiselect
    selected_attributes = st.multiselect("Seleccione los atributos cuyos modificadores desea utilizar:", options = abilities + ["Sin Modificador"])

    # Calculate and display selected modifiers
    if selected_attributes:
        st.write("Modificadores seleccionados:")
        for attr in selected_attributes:
            if attr == "Sin Modificador":
                mod = 0
                st.write(f"{attr}: {mod}")
            elif attr in ["Magia", "Competencia"]:
                mod = abilities_values[attr]
                st.write(f"{attr}: {mod}")
            else:
                mod = calcular_modificador(abilities_values[attr])
                st.write(f"{attr}: {mod}")
    else:
        st.write("No se han seleccionado atributos.")

if __name__ == "__main__":
    main()

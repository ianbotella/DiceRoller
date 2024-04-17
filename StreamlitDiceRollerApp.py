import streamlit as st

def calcular_modificador(value):
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
        return 0

def main():
    st.sidebar.title("Ingrese Valores de Atributos")

    # Diccionario para almacenar los valores y modificadores
    atributos = {
        "Fuerza": 0,
        "Destreza": 0,
        "Constitucion": 0,
        "Inteligencia": 0,
        "Sabiduria": 0,
        "Carisma": 0,
        "Magia": 0, # Sin conversion
        "Competencia": 0 # Sin conversion
    }

    # Crear entradas para cada atributo y calcular modificadores
    for atributo in atributos.keys():
        valor = st.sidebar.number_input(f"Valor de {atributo}", min_value=1, max_value=30, value=10, step=1)
        if atributo in ["Magia", "Competencia"]:
            # Estos atributos no usan la funcion de conversion
            modificadores = valor
        else:
            # Los demas atributos usan la funcion de conversion
            modificadores = calcular_modificador(valor)
        st.sidebar.write(f"Modificador de {atributo}: {modificadores}")

if __name__ == "__main__":
    main()

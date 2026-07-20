import streamlit as st
from core.models import Filamento, ColorBase

def cargar_catalogo_materiales():
    return {
        "PLA": ["Plus (+)", "Silk", "Matte"],
        "PETG": ["Normal", "HS", "Metalizado"],
        "TPU": ["Normal"],
        "ABS": ["Normal"],
        "ASA": ["Normal"],
        "NYLON": ["Normal"]
    }

def cargar_base_colores():
    return [
        ColorBase("Negro", "#000000"),
        ColorBase("Blanco", "#FFFFFF"),
        ColorBase("Rojo", "#FF0000"),
        ColorBase("Azul", "#0000FF"),
        ColorBase("Verde Oliva", "#556B2F"),
        ColorBase("Verde Musgo", "#4A5D23"),
        ColorBase("Verde Lima", "#32CD32"),
        ColorBase("Verde Manzana", "#8DB600"),
        ColorBase("Amarillo", "#FFFF00"),
        ColorBase("Dorado", "#DAA520"),
        ColorBase("Plateado", "#C0C0C0"),
    ]

def render():
    st.title("Agregar Filamento")

    materiales = cargar_catalogo_materiales()
    base_colores = cargar_base_colores()

    if "filamentos" not in st.session_state:
        st.session_state.filamentos = []

    material = st.selectbox("Material", list(materiales.keys()))
    tipo = st.selectbox("Tipo", materiales[material])

    color_nombre = st.text_input("Nombre del color")
    color_hex = st.color_picker("Color visual")

    marca = st.selectbox("Marca", ["eSun", "Otra marca"])
    if marca == "Otra marca":
        marca = st.text_input("Nombre de la marca")

    gramos = st.number_input("Gramos del rollo", 0.0, step=1.0)
    costo_total = st.number_input("Costo total del rollo (Q)", 0.0, step=0.01)

    if st.button("Agregar"):
        if gramos <= 0 or costo_total <= 0:
            st.error("Los gramos y el costo deben ser mayores a 0.")
            return

        costo_por_gramo = costo_total / gramos

        nuevo = Filamento(
            material=material,
            tipo=tipo,
            color_nombre=color_nombre,
            color_hex=color_hex,
            marca=marca,
            gramos=gramos,
            costo_total=costo_total,
            costo_por_gramo=costo_por_gramo
        )

        for f in st.session_state.filamentos:
            if (
                f.material == nuevo.material and
                f.tipo == nuevo.tipo and
                f.color_nombre.lower() == nuevo.color_nombre.lower() and
                f.color_hex == nuevo.color_hex and
                f.marca.lower() == nuevo.marca.lower()
            ):
                if f.gramos != nuevo.gramos or f.costo_total != nuevo.costo_total:
                    st.warning("Este filamento ya existe. ¿Deseas actualizar el precio del filamento existente o agregarlo como variante?")
                    col1, col2 = st.columns(2)

                    if col1.button("Actualizar precio"):
                        f.gramos = nuevo.gramos
                        f.costo_total = nuevo.costo_total
                        f.costo_por_gramo = nuevo.costo_por_gramo
                        f.color_hex = nuevo.color_hex
                        f.marca = nuevo.marca
                        st.success("Filamento actualizado.")
                        return

                    if col2.button("Agregar variante"):
                        st.session_state.filamentos.append(nuevo)
                        st.success("Variante agregada.")
                        return

                    return

                st.error("Este filamento ya existe en tu inventario.")
                return

        st.session_state.filamentos.append(nuevo)
        st.success("Filamento agregado correctamente.")

render()

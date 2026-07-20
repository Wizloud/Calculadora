import streamlit as st
from core.models import Filamento

def render():
    st.title("Inventario de Filamentos")

    if "filamentos" not in st.session_state:
        st.session_state.filamentos = []

    st.write("### Filamentos registrados")

    if not st.session_state.filamentos:
        st.info("No tienes filamentos registrados aún.")
    else:
        tabla = []
        for idx, f in enumerate(st.session_state.filamentos):
            tabla.append({
                "Nombre": f"{f.material} {f.tipo} {f.color_nombre} ({f.marca})",
                "Color": f.color_hex,
                "Gramos": f.gramos,
                "Costo total (Q)": f.costo_total,
                "Costo por gramo (Q)": round(f.costo_por_gramo, 3)
            })

        st.dataframe(tabla, use_container_width=True)

        eliminar_idx = st.selectbox(
            "Eliminar filamento",
            options=list(range(len(st.session_state.filamentos))),
            format_func=lambda i: f"{st.session_state.filamentos[i].material} {st.session_state.filamentos[i].tipo} {st.session_state.filamentos[i].color_nombre} ({st.session_state.filamentos[i].marca})"
        )

        if st.button("Eliminar"):
            st.session_state.filamentos.pop(eliminar_idx)
            st.success("Filamento eliminado.")

    st.write("---")
    st.page_link("pages/agregar_filamento.py", label="➕ Agregar filamento")

render()

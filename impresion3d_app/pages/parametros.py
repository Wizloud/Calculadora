import streamlit as st

def render():
    st.title("Parámetros globales")

    if "parametros" not in st.session_state:
        st.session_state.parametros = {
            "electricidad": 0.0,
            "depreciacion": 0.0,
            "postproceso": 0.0,
            "costos_fijos": 0.0,
            "margen": 40.0,
            "iva": 12.0,
        }

    p = st.session_state.parametros

    p["electricidad"] = st.number_input("Costo electricidad por hora (Q)", p["electricidad"])
    p["depreciacion"] = st.number_input("Costo depreciación por hora (Q)", p["depreciacion"])
    p["postproceso"] = st.number_input("Costo postproceso por hora (Q)", p["postproceso"])
    p["costos_fijos"] = st.number_input("Costos fijos (Q)", p["costos_fijos"])
    p["margen"] = st.number_input("Margen (%)", p["margen"])
    p["iva"] = st.number_input("IVA (%)", p["iva"])

    st.success("Parámetros actualizados.")

render()

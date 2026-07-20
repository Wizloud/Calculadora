import streamlit as st

def render():
    st.title("Cotización")

    filamentos = st.session_state.get("filamentos", [])
    parametros = st.session_state.get("parametros", None)

    if not filamentos:
        st.warning("No tienes filamentos registrados.")
        return

    if not parametros:
        st.warning("No has configurado los parámetros globales.")
        return

    filamento_sel = st.selectbox(
        "Filamento",
        options=filamentos,
        format_func=lambda f: f"{f.material} {f.tipo} {f.color_nombre} ({f.marca})"
    )

    gramos_impresos = st.number_input("Gramos usados", 0.0, step=0.1)
    tiempo_impresion = st.number_input("Tiempo de impresión (h)", 0.0, step=0.1)
    tiempo_diseno = st.number_input("Tiempo de diseño (h)", 0.0, step=0.1)
    tiempo_postproceso = st.number_input("Tiempo de postproceso (h)", 0.0, step=0.1)

    if st.button("Generar cotización"):
        costo_por_gramo = filamento_sel.costo_por_gramo
        p = parametros

        costo_material = gramos_impresos * costo_por_gramo
        costo_electricidad = tiempo_impresion * p["electricidad"]
        costo_depreciacion = tiempo_impresion * p["depreciacion"]
        costo_postproceso = tiempo_postproceso * p["postproceso"]
        costos_fijos = p["costos_fijos"]

        subtotal = (
            costo_material +
            costo_electricidad +
            costo_depreciacion +
            costo_postproceso +
            costos_fijos
        )

        precio_con_margen = subtotal * (1 + p["margen"] / 100)
        precio_final = precio_con_margen * (1 + p["iva"] / 100)

        st.write("---")
        st.subheader("Resumen para cliente")

        st.write(f"**Filamento:** {filamento_sel.material} {filamento_sel.tipo} {filamento_sel.color_nombre} ({filamento_sel.marca})")
        st.write(f"**Gramos usados:** {gramos_impresos:.1f} g")
        st.write(f"**Tiempo impresión:** {tiempo_impresion:.1f} h")
        st.write(f"**Tiempo diseño:** {tiempo_diseno:.1f} h")
        st.write(f"**Tiempo postproceso:** {tiempo_postproceso:.1f} h")

        st.write(f"**Precio final (con IVA): Q {precio_final:.2f}**")

render()

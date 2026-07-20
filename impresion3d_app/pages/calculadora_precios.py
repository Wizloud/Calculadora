import streamlit as st

def render():
    st.title("Calculadora de precios")

    filamentos = st.session_state.get("filamentos", [])

    if not filamentos:
        st.warning("No tienes filamentos registrados.")
        return

    filamento_sel = st.selectbox(
        "Filamento",
        options=filamentos,
        format_func=lambda f: f"{f.material} {f.tipo} {f.color_nombre} ({f.marca})"
    )

    costo_por_gramo = filamento_sel.costo_por_gramo
    st.write(f"Costo por gramo: **Q {costo_por_gramo:.3f}**")

    st.write("---")
    st.subheader("Datos de impresión")

    gramos_impresos = st.number_input("Gramos usados", 0.0, step=0.1)
    tiempo_impresion = st.number_input("Tiempo de impresión (h)", 0.0, step=0.1)
    tiempo_diseno = st.number_input("Tiempo de diseño (h)", 0.0, step=0.1)
    tiempo_postproceso = st.number_input("Tiempo de postproceso (h)", 0.0, step=0.1)

    parametros = st.session_state.get("parametros", {
        "electricidad": 0.0,
        "depreciacion": 0.0,
        "postproceso": 0.0,
        "costos_fijos": 0.0,
        "margen": 40.0,
        "iva": 12.0,
    })

    st.write("---")
    st.subheader("Resumen de costos")

    costo_material = gramos_impresos * costo_por_gramo
    costo_electricidad = tiempo_impresion * parametros["electricidad"]
    costo_depreciacion = tiempo_impresion * parametros["depreciacion"]
    costo_postproceso = tiempo_postproceso * parametros["postproceso"]
    costos_fijos = parametros["costos_fijos"]

    subtotal = (
        costo_material +
        costo_electricidad +
        costo_depreciacion +
        costo_postproceso +
        costos_fijos
    )

    precio_con_margen = subtotal * (1 + parametros["margen"] / 100)
    precio_final = precio_con_margen * (1 + parametros["iva"] / 100)

    st.write(f"Costo material: **Q {costo_material:.2f}**")
    st.write(f"Costo electricidad: **Q {costo_electricidad:.2f}**")
    st.write(f"Costo depreciación: **Q {costo_depreciacion:.2f}**")
    st.write(f"Costo postproceso: **Q {costo_postproceso:.2f}**")
    st.write(f"Costos fijos: **Q {costos_fijos:.2f}**")
    st.write(f"Subtotal: **Q {subtotal:.2f}**")
    st.write(f"Precio con margen: **Q {precio_con_margen:.2f}**")
    st.write(f"Precio final con IVA: **Q {precio_final:.2f}**")

render()

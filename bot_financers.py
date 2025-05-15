import streamlit as st

st.title("Simulador Bot Comercial - FINANCERS")

intencion = st.selectbox("¿Qué servicio necesita el cliente?", ["", "Abrir LLC", "Declarar impuestos", "Abrir cuenta bancaria"])

estado = None
tipo = None

if intencion == "Abrir LLC":
    estado = st.selectbox("¿En qué estado desea abrir la LLC?", ["", "New Mexico", "Florida"])
    tipo = st.selectbox("¿Qué tipo de LLC es?", ["", "Single Member", "Multi Member"])

elif intencion == "Declarar impuestos":
    tipo = st.selectbox("¿Qué tipo de LLC tiene?", ["", "Single Member", "Multi Member"])

respuestas = {
    "llc_new_mexico_single": {
        "respuesta": "Perfecto. Para una LLC Single Member en New Mexico, tenés una opción muy económica, sin publicación de datos y sin mantenimiento anual obligatorio.",
        "pdf": "Presupuesto SM - New Mexico.pdf",
        "calendly": "https://calendly.com/financers/llamada"
    },
    "llc_florida_multi": {
        "respuesta": "Excelente. Para una LLC Multi Member en Florida (ideal para real estate), te paso el presupuesto y te recomiendo considerar también una estructura offshore para evitar el Estate Tax.",
        "pdf": "Presupuesto MM - Florida.pdf",
        "calendly": "https://calendly.com/financers/llamada",
        "extra": "https://www.financers.com.ar/estructura-en-bvi-para-evitar-el-estate-inheritance-tax-en-usa/"
    },
    "impuestos_single": {
        "respuesta": "Una LLC Single Member debe presentar el formulario 5472 y mantener libro contable. Si no se presenta, la multa puede ser de $25,000.",
        "calendly": "https://calendly.com/financers/llamada"
    },
    "cuenta_sin_llc": {
        "respuesta": "Para abrir una cuenta bancaria en EE.UU., primero necesitás una LLC y el EIN. Podemos ayudarte con eso.",
        "calendly": "https://calendly.com/financers/llamada"
    }
}

def obtener_respuesta(intencion, estado=None, tipo=None):
    if intencion == "Abrir LLC":
        if estado == "New Mexico" and tipo == "Single Member":
            return respuestas["llc_new_mexico_single"]
        elif estado == "Florida" and tipo == "Multi Member":
            return respuestas["llc_florida_multi"]
    elif intencion == "Declarar impuestos":
        if tipo == "Single Member":
            return respuestas["impuestos_single"]
    elif intencion == "Abrir cuenta bancaria":
        return respuestas["cuenta_sin_llc"]
    return {"respuesta": "Podés contarme un poco más sobre tu caso así te oriento mejor."}

if st.button("Ver respuesta del bot"):
    resultado = obtener_respuesta(intencion, estado, tipo)
    st.write("**Respuesta del bot:**")
    st.write(resultado["respuesta"])
    if "pdf" in resultado:
        st.write(f"**PDF sugerido:** {resultado['pdf']}")
    if "extra" in resultado:
        st.write(f"**Artículo adicional:** {resultado['extra']}")
    st.write(f"**Agendá tu llamada:** {resultado['calendly']}")

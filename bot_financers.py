import streamlit as st

st.title("Asesor Virtual - FINANCERS")

st.markdown("Ayudamos a extranjeros a operar legalmente en EE.UU. con soluciones simples, seguras y claras.")
st.markdown("Seleccioná el servicio sobre el cual querés recibir información:")

intencion = st.selectbox("¿Qué te interesa hacer?", [
    "", "Abrir una LLC", "Declarar impuestos", "Abrir una cuenta bancaria", "Enviar una consulta personalizada"
])

estado = tipo = None

if intencion == "Abrir una LLC":
    conocimiento = st.radio("¿Tenés conocimiento previo sobre las LLC en EE.UU.?", ["Sí", "No"])
    if conocimiento == "Sí":
        estado = st.selectbox("¿En qué estado querés abrirla?", ["", "Florida", "Delaware", "New Mexico", "Wyoming"])
        tipo = st.selectbox("¿La manejarás solo o con otros socios?", ["", "Single Member", "Multi Member"])
    elif conocimiento == "No":
        st.markdown("**Estados recomendados:**")
        st.markdown("- **New Mexico:** Bajo costo, simple, ideal para operar online.")
        st.markdown("- **Florida:** Excelente para real estate y cuentas bancarias.")
        st.markdown("- **Delaware:** Prestigio legal, ideal si buscás escalar o atraer inversión.")
        st.markdown("¿Querés contarnos si vas a comprar un inmueble o operar online?")
        tipo = st.selectbox("¿La manejarás solo o con otros socios?", ["", "Single Member", "Multi Member"])

elif intencion == "Declarar impuestos":
    tiene_llc = st.radio("¿Ya tenés una LLC formada?", ["Sí", "No"])
    if tiene_llc == "Sí":
        tipo = st.selectbox("¿Tu LLC es Single Member o Multi Member?", ["", "Single Member", "Multi Member"])
    else:
        st.warning("Para declarar impuestos primero debés tener una LLC. Podemos ayudarte con la apertura.")

elif intencion == "Abrir una cuenta bancaria":
    tiene_llc = st.radio("¿Ya tenés una LLC formada con EIN?", ["Sí", "No"])
    if tiene_llc == "No":
        st.warning("Para abrir una cuenta bancaria necesitás una LLC registrada y el EIN. Podemos ayudarte con eso.")
    else:
        st.markdown("Podemos ayudarte a abrir cuentas en:")
        st.markdown("- **Mercury:** 100% online, sin presencialidad")
        st.markdown("- **Relay:** multiusuario, ideal para equipos")
        st.markdown("- Bancos físicos en EE.UU. si tenés dirección o visita programada")

elif intencion == "Enviar una consulta personalizada":
    st.subheader("Dejanos tu consulta y te contactamos personalmente")
    nombre = st.text_input("Nombre completo")
    contacto = st.text_input("Correo electrónico o WhatsApp")
    consulta = st.text_area("Escribí tu consulta")

    if st.button("Enviar consulta"):
        if nombre and contacto and consulta:
            st.success("Gracias. Nuestro equipo se pondrá en contacto en breve.")
            st.markdown(f"**Resumen:**\n\nNombre: {nombre}\nContacto: {contacto}\nConsulta: {consulta}")
        else:
            st.warning("Por favor completá todos los campos.")

# RESPUESTAS DETALLADAS

respuestas = {
    "llc_florida_single": (
        "**LLC Single Member en Florida**\n\n"
        "- Costo total estimado: USD 739\n"
        "- Ideal para inversiones inmobiliarias y apertura de cuenta bancaria\n"
        "- Buena reputación legal y reconocimiento internacional\n"
        "- Atención: puede aplicar Estate Tax (hasta 40%) si no se usa una estructura offshore\n\n"
        "**PDF sugerido:** Presupuesto SM - Florida.pdf\n"
        "**Artículo:** https://www.financers.com.ar/estructura-en-bvi-para-evitar-el-estate-inheritance-tax-en-usa/\n"
        "**Agendá tu llamada:** https://calendly.com/financers/llamada"
    ),
    "llc_florida_multi": (
        "**LLC Multi Member en Florida**\n\n"
        "- Costo estimado: USD 1040\n"
        "- Requiere Formulario 1065 + K-1 por socio\n"
        "- Recomendamos estructura offshore si hay real estate y socios extranjeros\n\n"
        "**PDF sugerido:** Presupuesto MM - Florida.pdf\n"
        "**Agendá tu llamada:** https://calendly.com/financers/llamada"
    ),
    "llc_new_mexico_single": (
        "**LLC Single Member en New Mexico**\n\n"
        "- Costo estimado: USD 589\n"
        "- No requiere publicación de miembros\n"
        "- Ideal para freelancers, consultores y operaciones online\n"
        "- Mantenimiento anual bajo\n\n"
        "**PDF sugerido:** Presupuesto SM - New Mexico.pdf\n"
        "**Agendá tu llamada:** https://calendly.com/financers/llamada"
    ),
    "llc_delaware_single": (
        "**LLC Single Member en Delaware**\n\n"
        "- Costo estimado: USD 739\n"
        "- Prestigio legal a nivel internacional\n"
        "- Recomendado para startups, tecnología y negocios con socios\n\n"
        "**PDF sugerido:** Presupuesto SM - Delaware.pdf\n"
        "**Agendá tu llamada:** https://calendly.com/financers/llamada"
    ),
    "impuestos_single": (
        "**Declaración de impuestos – LLC Single Member**\n\n"
        "- Formulario 5472 + libro contable obligatorio\n"
        "- Si hubo ingresos, presentar Schedule C\n"
        "- Multa por no presentar: hasta USD 25.000\n"
        "- Tiempo estimado: 3 a 5 días hábiles\n\n"
        "**Agendá tu llamada:** https://calendly.com/financers/llamada"
    ),
    "impuestos_multi": (
        "**Declaración de impuestos – LLC Multi Member**\n\n"
        "- Formulario 1065 obligatorio\n"
        "- Cada socio debe recibir un K-1\n"
        "- W-8BEN-E si los socios son extranjeros\n"
        "- Multa por no presentar: USD 210 por socio por mes\n\n"
        "**Agendá tu llamada:** https://calendly.com/financers/llamada"
    ),
    "cuenta_sin_llc": (
        "**Apertura de cuenta bancaria**\n\n"
        "- Requiere LLC + EIN\n"
        "- Podemos ayudarte a abrir cuenta en Mercury, Relay o bancos físicos\n"
        "- Si no tenés estructura, sugerimos abrir primero una LLC\n\n"
        "**Agendá tu llamada:** https://calendly.com/financers/llamada"
    )
}

def generar_respuesta(intencion, estado=None, tipo=None):
    key = ""
    if intencion == "Abrir una LLC" and estado and tipo:
        key = f"llc_{estado.lower().replace(' ', '_')}_{tipo.lower().split()[0]}"
    elif intencion == "Declarar impuestos" and tipo:
        key = f"impuestos_{tipo.lower().split()[0]}"
    elif intencion == "Abrir una cuenta bancaria":
        key = "cuenta_sin_llc"
    return respuestas.get(key, "Podés contarnos un poco más sobre tu caso así te orientamos mejor.")

# Mostrar respuesta si corresponde
if intencion in ["Abrir una LLC", "Declarar impuestos", "Abrir una cuenta bancaria"]:
    if st.button("Ver respuesta detallada"):
        resultado = generar_respuesta(intencion, estado, tipo)
        st.markdown("### Resultado")
        st.markdown(resultado)

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
        st.markdown("### ¿Qué es una LLC y por qué puede servirte?")
        st.markdown(
            "- Una LLC (Limited Liability Company) es una estructura legal que permite a extranjeros abrir una empresa en EE.UU. sin necesidad de residencia ni visa.\n"
            "- Es útil para vender servicios online, hacer inversiones inmobiliarias, operar un e-commerce o abrir una cuenta bancaria.\n"
            "- Protege tu patrimonio personal, permite operar en dólares, emitir facturas y no tributar en EE.UU. si no hay actividad allí.\n"
            "- ¿Querés saber si te conviene abrir una LLC en tu caso particular?"
        )
        st.markdown("👉 [Agendá una llamada sin compromiso](https://calendly.com/financers/llamada)")

elif intencion == "Declarar impuestos":
    tiene_llc = st.radio("¿Ya tenés una LLC formada?", ["Sí", "No"])
    if tiene_llc == "Sí":
        st.markdown("¿Podés confirmarme lo siguiente?")
        estado = st.selectbox("¿En qué estado está registrada tu LLC?", ["", "Florida", "Delaware", "New Mexico", "Wyoming"])
        tipo = st.selectbox("¿Es Single Member o Multi Member?", ["", "Single Member", "Multi Member"])
        st.radio("¿Tiene bienes o activos a su nombre?", ["Sí", "No"])
        st.radio("¿Tributa como LLC o como Corporación?", ["LLC", "C-Corp", "No lo sé"])
    else:
        st.warning("Para declarar impuestos primero debés tener una LLC. Podemos ayudarte con la apertura.")

elif intencion == "Abrir una cuenta bancaria":
    tiene_llc = st.radio("¿Ya tenés una LLC con EIN?", ["Sí", "No"])
    if tiene_llc == "Sí":
        st.markdown("### Opciones disponibles:")
        st.markdown("- **Mercury o Relay:** 100% online, sin depósito mínimo – Costo: USD 250")
        st.markdown("- **OceanBank o IFB:** mínimo USD 10.000 a 25.000 – Costo: USD 1500")
        st.markdown("¿Preferís que avancemos con alguna opción o querés agendar una videollamada?")
    else:
        st.warning("Para abrir una cuenta bancaria necesitás una LLC y EIN. Podemos ayudarte con todo el proceso.")

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

# RESPUESTAS DETALLADAS PARA DECLARACIÓN DE IMPUESTOS
if intencion == "Declarar impuestos" and estado and tipo:
    st.markdown("### Detalles para tu LLC")

    if estado == "Florida":
        if tipo == "Single Member":
            st.markdown(
                "- **Costo declaración IRS:** USD 500\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Sunbiz): USD 139\n"
                "- PDF: Presupuesto Florida SM"
            )
        else:
            st.markdown(
                "- **Costo declaración IRS:** USD 800\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Sunbiz): USD 139\n"
                "- PDF: Presupuesto Florida MM"
            )

    elif estado == "New Mexico":
        if tipo == "Single Member":
            st.markdown(
                "- **Costo declaración IRS:** USD 500\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Renovación): USD 0\n"
                "- PDF: Presupuesto NM SM"
            )
        else:
            st.markdown(
                "- **Costo declaración IRS:** USD 800\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Renovación): USD 0\n"
                "- PDF: Presupuesto NM MM"
            )

    elif estado == "Wyoming":
        if tipo == "Single Member":
            st.markdown(
                "- **Costo declaración IRS:** USD 500\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Renovación): USD 62\n"
                "- PDF: Presupuesto WY SM"
            )
        else:
            st.markdown(
                "- **Costo declaración IRS:** USD 800\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Renovación): USD 62\n"
                "- PDF: Presupuesto WY MM"
            )

    elif estado == "Delaware":
        if tipo == "Single Member":
            st.markdown(
                "- **Costo declaración IRS:** USD 500\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Franchise Tax): USD 300\n"
                "- PDF: Presupuesto DE SM"
            )
        else:
            st.markdown(
                "- **Costo declaración IRS:** USD 800\n"
                "- Agente registrado: USD 100\n"
                "- Impuesto estatal (Franchise Tax): USD 300\n"
                "- PDF: Presupuesto DE MM"
            )

st.markdown("---")
st.markdown("**Nota importante:** Si no estás más de 183 días en EE.UU., no generás ingresos conectados a suelo americano (ECI), y tus ingresos no son de fuente estadounidense, no debés tributar. Pero sí debés presentar la declaración anual ante el IRS.")
st.markdown("**Además:** Si tuvieras inmuebles o empleados en EE.UU., ahí sí deberías tributar y lo ideal sería una C-Corp que paga 21% de impuesto.")

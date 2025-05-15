import streamlit as st

st.title("Asesor Virtual - FINANCERS")

st.markdown("Ayudamos a extranjeros a operar legalmente en EE.UU. con soluciones simples, seguras y claras.")
st.markdown("Seleccioná el servicio sobre el cual querés recibir información:")

intencion = st.selectbox("¿Qué te interesa hacer?", [
    "", "Abrir una LLC", "Declarar impuestos", "Abrir una cuenta bancaria", "Enviar una consulta personalizada"
])

estado = tipo = None

# === SECCIÓN ABRIR UNA LLC ===
if intencion == "Abrir una LLC":
    conocimiento = st.radio("¿Tenés conocimiento previo sobre las LLC en EE.UU.?", ["Sí", "No"])

    if conocimiento == "No":
        st.markdown("### ¿Qué es una LLC y por qué puede servirte?")
        st.markdown(
            "- Una **LLC** (Limited Liability Company) es una empresa legal en EE.UU. que podés abrir sin vivir en el país.\n"
            "- Te permite facturar en dólares, vender servicios o productos online, invertir en inmuebles o abrir cuentas bancarias.\n"
            "- Si no tenés actividad física ni ingresos conectados en EE.UU., no pagás impuestos, solo presentás declaración anual.\n"
            "- Protege tu patrimonio personal y te conecta con el sistema financiero global."
        )
        st.markdown("👉 [Agendá una llamada sin compromiso para evaluar tu caso](https://calendly.com/financers/llamada)")

    elif conocimiento == "Sí":
        estado = st.selectbox("¿En qué estado querés abrir la LLC?", ["", "Florida", "Delaware", "New Mexico"])
        tipo = st.selectbox("¿La manejarás solo o con otros socios?", ["", "Single Member", "Multi Member"])

        if estado and tipo:
            st.markdown("### Resumen de costos y beneficios")

            if estado == "Florida":
                if tipo == "Single Member":
                    st.markdown(
                        "- Costo de apertura: USD 1000 (incluye cuenta bancaria, BOI y BE-13)\n"
                        "- Gastos anuales: Sunbiz USD 139 + agente registrado USD 100\n"
                        "- Declaración IRS: USD 500\n"
                        "- PDF: Presupuesto SM - Florida\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
                else:
                    st.markdown(
                        "- Costo de apertura: USD 1000 (incluye cuenta bancaria, BOI y BE-13)\n"
                        "- Gastos anuales: Sunbiz USD 139 + agente registrado USD 100\n"
                        "- Declaración IRS: USD 800\n"
                        "- PDF: Presupuesto MM - Florida\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )

            elif estado == "New Mexico":
                if tipo == "Single Member":
                    st.markdown(
                        "- Costo de apertura: USD 700 (incluye cuenta bancaria, BOI y BE-13)\n"
                        "- Gastos anuales: solo agente registrado USD 100 (no hay impuesto estatal)\n"
                        "- Declaración IRS: USD 500\n"
                        "- PDF: Presupuesto SM - New Mexico\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
                else:
                    st.markdown(
                        "- Costo de apertura: USD 700 (incluye cuenta bancaria, BOI y BE-13)\n"
                        "- Gastos anuales: solo agente registrado USD 100 (no hay impuesto estatal)\n"
                        "- Declaración IRS: USD 800\n"
                        "- PDF: Presupuesto MM - New Mexico\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )

            elif estado == "Delaware":
                if tipo == "Single Member":
                    st.markdown(
                        "- Costo de apertura: USD 1300 (incluye cuenta bancaria, BOI y BE-13)\n"
                        "- Gastos anuales: Franchise Tax USD 300 + agente registrado USD 100\n"
                        "- Declaración IRS: USD 500\n"
                        "- PDF: Presupuesto SM - Delaware\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
                else:
                    st.markdown(
                        "- Costo de apertura: USD 1400 (incluye cuenta bancaria, BOI y BE-13)\n"
                        "- Gastos anuales: Franchise Tax USD 300 + agente registrado USD 100\n"
                        "- Declaración IRS: USD 800\n"
                        "- PDF: Presupuesto MM - Delaware\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )

# === SECCIÓN DECLARAR IMPUESTOS ===
elif intencion == "Declarar impuestos":
    tiene_llc = st.radio("¿Ya tenés una LLC formada?", ["Sí", "No"])
    if tiene_llc == "Sí":
        st.markdown("¿Podés confirmarme lo siguiente?")
        estado = st.selectbox("¿En qué estado está registrada tu LLC?", ["", "Florida", "Delaware", "New Mexico", "Wyoming"])
        tipo = st.selectbox("¿Es Single Member o Multi Member?", ["", "Single Member", "Multi Member"])
        st.radio("¿Tiene bienes o activos a su nombre?", ["Sí", "No"])
        st.radio("¿Tributa como LLC o como Corporación?", ["LLC", "C-Corp", "No lo sé"])

        if estado and tipo:
            st.markdown("### Costos y obligaciones para tu declaración:")
            if tipo == "Single Member":
                st.markdown("- **Declaración ante el IRS:** USD 500")
            else:
                st.markdown("- **Declaración ante el IRS:** USD 800")
            if estado == "Florida":
                st.markdown("- Agente registrado: USD 100\n- Impuesto estatal (Sunbiz): USD 139")
            elif estado == "New Mexico":
                st.markdown("- Agente registrado: USD 100\n- Impuesto estatal: USD 0")
            elif estado == "Wyoming":
                st.markdown("- Agente registrado: USD 100\n- Impuesto estatal: USD 62")
            elif estado == "Delaware":
                st.markdown("- Agente registrado: USD 100\n- Franchise Tax: USD 300")

            st.markdown("[Agendá tu llamada para avanzar](https://calendly.com/financers/llamada)")

    else:
        st.warning("Para declarar impuestos necesitás tener una LLC. Podemos ayudarte con la apertura.")

# === SECCIÓN CUENTA BANCARIA ===
elif intencion == "Abrir una cuenta bancaria":
    tiene_llc = st.radio("¿Ya tenés una LLC con EIN?", ["Sí", "No"])
    if tiene_llc == "Sí":
        st.markdown("### Opciones disponibles:")
        st.markdown("- **Mercury o Relay:** 100% online, sin depósito mínimo – Costo: USD 250")
        st.markdown("- **OceanBank o IFB:** mínimo USD 10.000 a 25.000 – Costo: USD 1500")
        st.markdown("¿Querés avanzar con alguna opción o agendar una videollamada?")
        st.markdown("[Agendá una llamada](https://calendly.com/financers/llamada)")
    else:
        st.warning("Para abrir una cuenta bancaria necesitás una LLC con EIN. Podemos ayudarte con todo el proceso.")

# === SECCIÓN CONSULTA ABIERTA ===
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

# === NOTA LEGAL ===
st.markdown("---")
st.markdown("**Importante:** Si no estás más de 183 días en EE.UU., no generás ingresos conectados (ECI) ni ingresos de fuente estadounidense, no debés tributar. Aun así, debés presentar tu declaración anual ante el IRS.")
st.markdown("**Si tenés inmuebles o empleados en EE.UU.**, deberías tributar y lo recomendable sería una C-Corp (tasa fija del 21%), y abrir una sociedad offshore en caso de dedicarse a Real Estate o al mercado inmobiliario.")

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
            "- Una **LLC** (Limited Liability Company) es una empresa de EE.UU. que podés abrir sin vivir en el país ni tener visa.\n"
            "- Te permite facturar legalmente en dólares, abrir una cuenta bancaria, invertir en inmuebles o vender online.\n"
            "- Si no tenés presencia física ni generás ingresos en EE.UU., no pagás impuestos. Solo debés presentar una declaración anual.\n"
            "- Las LLC protegen tu patrimonio personal y te dan acceso a herramientas del sistema financiero estadounidense."
        )

        st.markdown("### Estados recomendados para abrir tu LLC:")
        st.markdown("**New Mexico** – Económica y privada\n- Costo apertura: USD 700\n- Sin impuestos estatales\n- Declaración: USD 500 si es SM")
        st.markdown("**Florida** – Ideal para Real Estate y bancos\n- Costo apertura: USD 1000\n- Gastos anuales: USD 139 + 100\n- Declaración: USD 500 / 800")
        st.markdown("**Delaware** – Prestigio internacional\n- Costo apertura: USD 1300 / 1400\n- Impuesto anual: USD 300 + 100\n- Declaración: USD 500 / 800")

        st.markdown("### ¿Querés que te ayudemos a elegir la mejor opción?")
        estado = st.selectbox("Seleccioná el estado que más te interesa:", ["", "Florida", "Delaware", "New Mexico"])
        tipo = st.selectbox("¿La manejarás solo o con otras personas?", ["", "Single Member", "Multi Member"])

        if estado and tipo:
            if estado == "Florida":
                if tipo == "Single Member":
                    st.markdown(
                        "**Resumen:** LLC en Florida (SM)\n\n"
                        "- Costo apertura: USD 1000 (incluye cuenta y BOI)\n"
                        "- Costos anuales: Sunbiz USD 139 + agente USD 100\n"
                        "- Declaración IRS: USD 500\n"
                        "- PDF: Presupuesto SM - Florida\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
                else:
                    st.markdown(
                        "**Resumen:** LLC en Florida (MM)\n\n"
                        "- Costo apertura: USD 1000 (incluye cuenta y BOI)\n"
                        "- Costos anuales: Sunbiz USD 139 + agente USD 100\n"
                        "- Declaración IRS: USD 800\n"
                        "- PDF: Presupuesto MM - Florida\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
            elif estado == "New Mexico":
                if tipo == "Single Member":
                    st.markdown(
                        "**Resumen:** LLC en New Mexico (SM)\n\n"
                        "- Costo apertura: USD 700 (incluye cuenta y BOI)\n"
                        "- Sin impuesto estatal anual (solo agente: USD 100)\n"
                        "- Declaración IRS: USD 500\n"
                        "- PDF: Presupuesto SM - New Mexico\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
                else:
                    st.markdown(
                        "**Resumen:** LLC en New Mexico (MM)\n\n"
                        "- Costo apertura: USD 700 (incluye cuenta y BOI)\n"
                        "- Sin impuesto estatal anual (solo agente: USD 100)\n"
                        "- Declaración IRS: USD 800\n"
                        "- PDF: Presupuesto MM - New Mexico\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
            elif estado == "Delaware":
                if tipo == "Single Member":
                    st.markdown(
                        "**Resumen:** LLC en Delaware (SM)\n\n"
                        "- Costo apertura: USD 1300 (incluye cuenta y BOI)\n"
                        "- Impuesto anual: Franchise Tax USD 300 + agente USD 100\n"
                        "- Declaración IRS: USD 500\n"
                        "- PDF: Presupuesto SM - Delaware\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )
                else:
                    st.markdown(
                        "**Resumen:** LLC en Delaware (MM)\n\n"
                        "- Costo apertura: USD 1400 (incluye cuenta y BOI)\n"
                        "- Impuesto anual: Franchise Tax USD 300 + agente USD 100\n"
                        "- Declaración IRS: USD 800\n"
                        "- PDF: Presupuesto MM - Delaware\n"
                        "[Agendá tu llamada](https://calendly.com/financers/llamada)"
                    )

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

elif intencion == "Abrir una cuenta bancaria":
    tiene_llc = st.radio("¿Ya tenés una LLC con EIN?", ["Sí", "No"])
    if tiene_llc == "Sí":
        st.markdown("### Opciones disponibles:")
        st.markdown("- **Mercury o Relay:** 100% online, sin depósito mínimo – Costo: USD 250")
        st.markdown("- **OceanBank o IFB:** mínimo USD 10.000 a 25.000 – Costo: USD 1500")
        st.markdown("¿Preferís que avancemos con alguna opción o querés agendar una videollamada?")
        st.markdown("[Agendá una llamada](https://calendly.com/financers/llamada)")
    else:
        st.warning("Para abrir una cuenta bancaria necesitás una LLC con EIN. Podemos ayudarte con todo el proceso.")

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

# Notas legales al pie
st.markdown("---")
st.markdown("**Importante:** Si no estás más de 183 días en EE.UU., no generás ingresos conectados (ECI) ni ingresos de fuente estadounidense, no debés tributar. Aun así, debés presentar tu declaración anual ante el IRS.")
st.markdown("**Si tenés inmuebles o empleados en EE.UU.**, deberías tributar y lo recomendable sería una C-Corp (tasa fija del 21%).")

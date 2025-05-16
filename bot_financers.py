import streamlit as st

st.title("Asesor Virtual - FINANCERS")

st.markdown("Ayudamos a extranjeros a operar legalmente en EE.UU. con soluciones simples, seguras y claras.")
st.markdown("Seleccioná el servicio sobre el cual querés recibir información:")

intencion = st.selectbox("¿Qué te interesa hacer?", [
    "", "Abrir una LLC", "Declarar impuestos", "Abrir una cuenta bancaria", "Enviar una consulta personalizada", "¿Quiénes somos?"
])

estado = tipo = None

respuestas = {
    "llc_florida_single": "- Costo total estimado: USD 739\n- Ideal para inversiones inmobiliarias y apertura de cuenta bancaria\n- Buena reputación legal y reconocimiento internacional\n- Atención: puede aplicar Estate Tax (hasta 40%) si no se usa una estructura offshore\n\n**PDF sugerido:** Presupuesto SM - Florida.pdf\n**Artículo:** https://www.financers.com.ar/estructura-en-bvi-para-evitar-el-estate-inheritance-tax-en-usa/\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "llc_florida_multi": "- Costo estimado: USD 1040\n- Requiere Formulario 1065 + K-1 por socio\n- Recomendamos estructura offshore si hay real estate y socios extranjeros\n\n**PDF sugerido:** Presupuesto MM - Florida.pdf\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "llc_new_mexico_single": "- Costo estimado: USD 589\n- No requiere publicación de miembros\n- Ideal para freelancers, consultores y operaciones online\n- Mantenimiento anual bajo\n\n**PDF sugerido:** Presupuesto SM - New Mexico.pdf\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "llc_new_mexico_multi": "- Costo estimado: USD 700\n- Incluye cuenta bancaria y encuestas obligatorias\n- Declaración IRS: USD 800\n- PDF: Presupuesto MM - New Mexico\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "llc_delaware_single": "- Costo estimado: USD 739\n- Prestigio legal a nivel internacional\n- Recomendado para startups, tecnología y negocios con socios\n\n**PDF sugerido:** Presupuesto SM - Delaware.pdf\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "llc_delaware_multi": "- Costo estimado: USD 1400\n- Incluye cuenta bancaria y encuestas obligatorias\n- Declaración IRS: USD 800\n- PDF: Presupuesto MM - Delaware\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "llc_wyoming_single": "- Costo estimado: USD 500\n- Privacidad y costos anuales bajos\n- Impuesto estatal: USD 62\n- Declaración IRS: USD 500\n- PDF: Presupuesto SM - Wyoming\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "llc_wyoming_multi": "- Costo estimado: USD 800\n- Agente registrado: USD 100\n- Impuesto estatal: USD 62\n- PDF: Presupuesto MM - Wyoming\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "impuestos_single": "- Formulario 5472 + libro contable obligatorio\n- Si hubo ingresos, presentar Schedule C\n- Multa por no presentar: hasta USD 25.000\n- Tiempo estimado: 3 a 5 días hábiles\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "impuestos_multi": "- Formulario 1065 obligatorio\n- Cada socio debe recibir un K-1\n- W-8BEN-E si los socios son extranjeros\n- Multa por no presentar: USD 210 por socio por mes\n**Agendá tu llamada:** https://calendly.com/financers/llamada",
    "cuenta_sin_llc": "- Requiere LLC + EIN\n- Podemos ayudarte a abrir cuenta en Mercury, Relay o bancos físicos\n- Si no tenés estructura, sugerimos abrir primero una LLC\n**Agendá tu llamada:** https://calendly.com/financers/llamada"
}

if intencion == "Abrir una LLC":
    conocimiento = st.radio("¿Tenés conocimiento previo sobre las LLC en EE.UU.?", ["Sí", "No"])

    if conocimiento == "No":
        st.markdown("### ¿Qué es una LLC y por qué puede servirte?")
        st.markdown(
            "- Una **LLC** (Limited Liability Company) es una empresa en EE.UU. que podés abrir sin vivir allá.\n"
            "- Te permite facturar en dólares, abrir una cuenta bancaria y operar legalmente.\n"
            "- Si no tenés actividad en EE.UU., no pagás impuestos, pero sí debés declarar anualmente.\n"
            "- Protege tu patrimonio personal y te conecta al sistema financiero global."
        )
        st.markdown("👉 [Agendá una llamada sin compromiso](https://calendly.com/financers/llamada)")

    elif conocimiento == "Sí":
        estado = st.selectbox("¿En qué estado querés abrirla?", ["", "Florida", "Delaware", "New Mexico", "Wyoming"])
        tipo = st.selectbox("¿La manejarás solo o con otros socios?", ["", "Single Member", "Multi Member"])

        if estado and tipo:
            key = f"llc_{estado.lower().replace(' ', '_')}_{tipo.lower().split()[0]}"
            if key in respuestas:
                st.markdown("### Resultado")
                st.markdown(respuestas[key])

elif intencion == "Declarar impuestos":
    tiene_llc = st.radio("¿Ya tenés una LLC formada?", ["Sí", "No"])
    if tiene_llc == "Sí":
        st.markdown("¿Podés confirmarme lo siguiente?")
        estado = st.selectbox("¿En qué estado está registrada tu LLC?", ["", "Florida", "Delaware", "New Mexico", "Wyoming"])
        tipo = st.selectbox("¿Es Single Member o Multi Member?", ["", "Single Member", "Multi Member"])
        activos = st.radio("¿Tu LLC tiene propiedades, cuentas o activos registrados a su nombre en EE.UU.?", ["Sí", "No"], help="Ej: inmuebles, autos, cuentas bancarias")

        if activos == "Sí":
            tipo_activo = st.radio("¿Incluye propiedades inmobiliarias o real estate?", ["Sí", "No"])
            if tipo_activo == "Sí":
                st.markdown("### Atención sobre propiedades inmobiliarias")
                st.markdown(
                    "- Si la LLC posee inmuebles en EE.UU., puede aplicar el **Estate Tax** (impuesto a la herencia de hasta 40%) en caso de fallecimiento del titular.\n"
                    "- Recomendamos en estos casos evaluar una **estructura offshore** (como una BVI) que sea dueña de la LLC para proteger el patrimonio.\n"
                    "- Además, podrías tributar si los ingresos se consideran **Effectively Connected Income (ECI)**.\n"
                    "\n**Artículo recomendado:** [Estructura para evitar Estate Tax](https://www.financers.com.ar/estructura-en-bvi-para-evitar-el-estate-inheritance-tax-en-usa/)"
                )

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
        st.warning("Para declarar impuestos primero debés tener una LLC. Podemos ayudarte con la apertura.")

elif intencion == "Abrir una cuenta bancaria":
    tiene_llc = st.radio("¿Ya tenés una LLC formada con EIN?", ["Sí", "No"])
    if tiene_llc == "No":
        st.warning("Para abrir una cuenta bancaria necesitás una LLC registrada y el EIN. Podemos ayudarte con eso.")
    else:
        st.markdown("Podemos ayudarte a abrir cuentas en:")
        st.markdown("- **Mercury:** 100% online, sin presencialidad")
        st.markdown("- **Relay:** multiusuario, ideal para equipos")
        st.markdown("- **OceanBank o IFB:** desde USD 10.000 a 25.000 de depósito mínimo – Costo de apertura: USD 1500")
        st.markdown("### Resultado")
        st.markdown(respuestas["cuenta_sin_llc"])

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

elif intencion == "¿Quiénes somos?":
    st.subheader("¿Quiénes somos en FINANCERS?")
    st.markdown(
        "Somos un equipo contable-financiero offshore en Estados Unidos y Argentina que colabora con inversores, empresas tecnológicas y estudios contables de Latinoamérica.

"
        "Nos especializamos en ofrecer soluciones para que puedas gestionar tu contabilidad en Estados Unidos de manera segura y confiable, hablando tu mismo idioma y permitiéndote trabajar con tranquilidad."
    )

elif intencion == "Preguntas frecuentes":
    st.subheader("Preguntas frecuentes")

    categorias = {
        "Apertura de LLC": [
            ("¿En qué estado me conviene crear la LLC?",
             "Depende del objetivo de tu negocio:

- **New Mexico** es ideal si buscás privacidad, bajo costo y no necesitás una imagen corporativa reconocida.
- **Florida** es excelente si vas a invertir en inmuebles, operar con cuentas bancarias locales o necesitás tener presencia en un estado comercialmente activo.
- **Delaware** es el más prestigioso desde el punto de vista legal. Muy recomendado para startups, empresas tecnológicas o si vas a levantar capital o tener inversores.

👉 [Agendá tu llamada](https://calendly.com/financers/llamada) para evaluar cuál te conviene."),
            ("¿Qué incluye el servicio de apertura?",
             "Nuestro servicio incluye:
- Registro legal
- EIN ante el IRS
- Agente registrado
- Operating Agreement
- Presentación BOI
- Asistencia para cuenta bancaria

👉 [Agendá tu llamada](https://calendly.com/financers/llamada)")
        ],
        "Declaración de impuestos": [
            ("¿Debo declarar si la LLC no tuvo movimientos?",
             "Sí. Si la LLC tiene EIN, está obligada a presentar declaración anual ante el IRS.
Incluso sin actividad, presentar 5472 (SM) o 1065+K-1 (MM).

👉 [Agendá tu llamada](https://calendly.com/financers/llamada) para evitar sanciones."),
            ("¿Cuál es el costo de la declaración anual?",
             "- SM: USD 500
- MM: USD 800
- RA: USD 100
- Impuesto estatal: Florida 139, Delaware 300, NM 0

👉 [Agendá tu llamada](https://calendly.com/financers/llamada)")
        ],
        "Cuenta bancaria": [
            ("¿Qué banco recomiendan?",
             "Recomendamos **Relay Financial**:
- Online
- Multiusuario
- Compatible con Stripe y Wise

👉 [Agendá tu llamada](https://calendly.com/financers/llamada) para ver si aplica a tu caso."),
            ("¿Qué necesito para abrir la cuenta?",
             "- LLC activa
- EIN
- Operating Agreement
- Pasaporte

👉 [Agendá tu llamada](https://calendly.com/financers/llamada)")
        ]
    }

    seccion = st.selectbox("Seleccioná una categoría", list(categorias.keys()))
    preguntas = [p[0] for p in categorias[seccion]]
    seleccion = st.selectbox("Seleccioná una pregunta", preguntas)

    for pregunta, respuesta in categorias[seccion]:
        if pregunta == seleccion:
            st.markdown(f"### {pregunta}")
            st.markdown(respuesta)
            break
    st.subheader("¿Quiénes somos en FINANCERS?")
    st.markdown(
        "Somos un equipo contable-financiero offshore en Estados Unidos y Argentina que colabora con inversores, empresas tecnológicas y estudios contables de Latinoamérica.\n\n"
        "Nos especializamos en ofrecer soluciones para que puedas gestionar tu contabilidad en Estados Unidos de manera segura y confiable, hablando tu mismo idioma y permitiéndote trabajar con tranquilidad."
    )

# Nota legal al pie
st.markdown("---")
st.markdown("**Importante:** Si no estás más de 183 días en EE.UU., no generás ingresos conectados (ECI) ni ingresos de fuente estadounidense, no debés tributar. Aun así, debés presentar tu declaración anual ante el IRS.")
st.markdown("**Si tenés inmuebles o empleados en EE.UU.**, deberías tributar y lo recomendable sería una C-Corp (tasa fija del 21%).")


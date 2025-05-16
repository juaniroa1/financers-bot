import streamlit as st

st.title("Asesor Virtual - FINANCERS")

st.markdown("Ayudamos a extranjeros a operar legalmente en EE.UU. con soluciones simples, seguras y claras.")
st.markdown("Seleccioná el servicio sobre el cual querés recibir información:")

intencion = st.selectbox("¿Cómo podemos ayudarte?", [
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

elif intencion == "Preguntas frecuentes":
    st.subheader("Preguntas frecuentes")

    categorias = {
        "Apertura de LLC": [
            ("¿En qué estado me conviene crear la LLC?",
             "Depende del objetivo de tu negocio:\n\n- **New Mexico** es ideal si buscás privacidad, bajo costo y no necesitás una imagen corporativa reconocida. No tiene impuestos estatales y es muy usado para e-commerce, servicios o actividades online.\n\n- **Florida** es excelente si vas a invertir en inmuebles, operar con cuentas bancarias locales o necesitás tener presencia en un estado comercialmente activo. Es el más elegido por quienes hacen real estate.\n\n- **Delaware** es el más prestigioso desde el punto de vista legal. Muy recomendado para startups, empresas tecnológicas o si vas a levantar capital o tener inversores.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) para evaluar cuál te conviene."),
            ("¿Qué incluye el servicio de apertura?",
             "Nuestro servicio es integral e incluye:\n\n- Redacción y presentación de los documentos ante el estado (Articles of Organization)\n- Obtención del número de identificación fiscal (EIN) ante el IRS\n- Inscripción del agente registrado (Registered Agent)\n- Envío de Operating Agreement y certificados\n- Asesoría para apertura de cuenta bancaria (Mercury, Relay u otras)\n- Presentación del BOI (reporte de beneficiarios)\n- Asistencia personalizada en español\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) para recibir el detalle según tu país y objetivo."),
            ("¿Qué significa ser Single Member o Multi Member?",
             "- **Single Member (SM):** la LLC tiene un solo dueño. Es más simple a nivel impositivo (formulario 5472 + 1120) y el costo de la declaración anual es menor (USD 500).\n\n- **Multi Member (MM):** la LLC tiene más de un socio. Se presenta un formulario 1065 y se entregan formularios K-1 a cada miembro. Costo aproximado: USD 800.\n\nLa estructura MM suele utilizarse si necesitás dividir responsabilidades, operar con socios o tener cuentas mancomunadas.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y evaluamos cuál te conviene."),
            ("¿La LLC permite recibir pagos internacionales?",
             "Sí. Una LLC en EE.UU. te permite operar con plataformas como Stripe, PayPal, Upwork, Deel, Wise, Binance, Coinbase y recibir pagos en USD.\n\nAdemás, podés emitir facturas desde la empresa para tus clientes en cualquier parte del mundo. Los fondos llegan a tu cuenta bancaria comercial en EE.UU. y desde allí los podés transferir a cualquier parte.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y te mostramos cómo operar con Stripe o Deel."),
            ("¿Qué costo tiene abrir una LLC?",
             "Depende del estado y tipo de estructura:\n\n- **New Mexico (SM):** desde USD 700\n- **Florida (SM):** USD 1000 + gastos anuales fijos (Sunbiz: 139, RA: 100)\n- **Delaware (SM):** USD 1300 + Franchise Tax: 300\n\nTodos los precios incluyen apertura de cuenta bancaria, presentación BOI y asesoría.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y te enviamos el presupuesto exacto según tu necesidad.")
        ],
        "Declaración de impuestos": [
            ("¿Debo declarar si la LLC no tuvo movimientos?",
             "Sí. Si tu LLC tiene EIN, está obligada a presentar declaración anual ante el IRS. No hacerlo puede generar multas importantes (USD 25.000 si sos Single Member).\n\nIncluso si no operaste, es obligatorio presentar el formulario 5472 (SM) o el 1065 + K-1 (MM).\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) para evitar sanciones."),
            ("¿Cuál es el costo de la declaración anual?",
             "- **LLC Single Member:** USD 500\n- **LLC Multi Member:** USD 800\n\nAdemás:\n- Agente registrado: USD 100/año\n- Impuesto estatal:\n  - New Mexico: 0\n  - Florida: 139\n  - Delaware: 300 (Franchise Tax)\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y te hacemos un presupuesto final."),
            ("¿Qué es el RA, Sunbiz o Franchise Tax?",
             "- **RA (Registered Agent):** es obligatorio y sirve como domicilio legal. USD 100/año.\n- **Sunbiz:** es el portal del estado de Florida donde renovás la existencia de la LLC. USD 139/año.\n- **Franchise Tax:** es el impuesto fijo anual que cobra Delaware. USD 300.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) si querés automatizar tus vencimientos."),
            ("¿Puedo pagarme un sueldo desde la LLC?",
             "Sí, pero depende de si sos residente fiscal o no:\n- Si **no** lo sos: podés transferirte dinero como **distribución de utilidades**, sin tributar en EE.UU.\n- Si **lo sos**: deberías registrarte como empleador y pagar impuestos laborales.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y analizamos tu caso fiscal."),
            ("¿Cómo declaro en Argentina los ingresos desde la LLC?",
             "Debés declarar en el Impuesto a las Ganancias como \"renta de fuente extranjera\".\n\nAdemás, si tenés participación societaria o cuentas bancarias en el exterior, podrían entrar en Bienes Personales. Recomendamos trabajar con un contador local que esté familiarizado con estructuras offshore.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y te derivamos a un contador especialista.")
        ],
        "Cuenta bancaria": [
            ("¿Qué banco recomiendan?",
             "Usamos **Relay Financial** como primera opción:\n- 100% online\n- Multiusuario\n- Integración con QuickBooks y herramientas contables\n- Permite recibir transferencias internacionales y pagos de Stripe o PayPal\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y te mostramos cómo abrirla."),
            ("¿Puedo abrir una cuenta como extranjero?",
             "Sí. No necesitás visa ni residencia. Solo necesitás:\n- Tu LLC activa\n- EIN\n- Pasaporte vigente\n- Operating Agreement y Articles of Organization\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y te acompañamos en el proceso."),
            ("¿Qué necesito para abrir la cuenta?",
             "- LLC ya constituida\n- EIN aprobado\n- Documentos legales (certificados y acuerdos)\n- Pasaporte\n- Completar formulario online (KYC)\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y te enviamos un ejemplo del formulario."),
            ("¿Puedo transferir fondos desde Argentina u otros países?",
             "Sí. La cuenta de Relay o Mercury permite recibir transferencias SWIFT desde cualquier país. También podés fondearla con Payoneer, Wise, Stripe u otros métodos.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) si querés verificar si tu banco es compatible."),
            ("¿Qué pasa si no puedo completar el onboarding?",
             "Nuestro equipo te asesora para corregir errores. Si Relay rechaza la solicitud, intentamos con Mercury o IFB/OceanBank.\n\n👉 [Agendá tu llamada](https://calendly.com/financers/llamada) y resolvemos juntos el onboarding.")
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


elif intencion == "¿Quiénes somos?":
    st.subheader("¿Quiénes somos en FINANCERS?")
    st.markdown(
        "Somos un equipo contable-financiero offshore en Estados Unidos y Argentina que colabora con inversores, empresas tecnológicas y estudios contables de Latinoamérica.\n\n"
        "Nos especializamos en ofrecer soluciones para que puedas gestionar tu contabilidad en Estados Unidos de manera segura y confiable, hablando tu mismo idioma y permitiéndote trabajar con tranquilidad."
    )



# Nota legal al pie
st.markdown("---")
st.markdown("**Importante:** Si no estás más de 183 días en EE.UU., no generás ingresos conectados (ECI) ni ingresos de fuente estadounidense, no debés tributar. Aun así, debés presentar tu declaración anual ante el IRS.")
st.markdown("**Si tenés inmuebles o empleados en EE.UU.**, deberías tributar y lo recomendable sería una C-Corp (tasa fija del 21%).")


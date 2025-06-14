import streamlit as st

st.title("Asesor Virtual - FINANCERS")

# 🔒 Ocultar menú superior, GitHub, Share, etc.
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton, .st-emotion-cache-1h0z5md {display: none !important;}
    .css-1lsmgbg.egzxvld1 {display: none;} /* Oculta el botón de editar */
    .css-h5rgaw {display: none;} /* Oculta el ícono de GitHub */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("Ayudamos a extranjeros a operar legalmente en EE.UU. con soluciones simples, seguras y claras.")
st.markdown("Seleccioná el servicio sobre el cual querés recibir información:")

intencion = st.selectbox("¿Cómo podemos ayudarte?", [
    "", "¿Quiénes somos?" ,"Abrir una LLC", "Declarar impuestos", "Abrir una cuenta bancaria", "Preguntas frecuentes"
])


estado = tipo = None

respuestas = {
    "llc_florida_single": "- Costo total estimado: USD 739\n- Ideal para inversiones inmobiliarias y apertura de cuenta bancaria\n- Buena reputación legal y reconocimiento internacional\n- Atención: puede aplicar Estate Tax (hasta 40%) si no se usa una estructura offshore\n\n**Artículo:** https://www.financers.com.ar/estructura-en-bvi-para-evitar-el-estate-inheritance-tax-en-usa/\n\n **Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "llc_florida_multi": "- Costo estimado: USD 1040\n- Requiere Formulario 1065 + K-1 por socio\n- Recomendamos estructura offshore si hay real estate y socios extranjeros\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "llc_new_mexico_single": "- Costo estimado: USD 589\n- No requiere publicación de miembros\n- Ideal para freelancers, consultores y operaciones online\n- Mantenimiento anual bajo\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "llc_new_mexico_multi": "- Costo estimado: USD 700\n- Incluye cuenta bancaria y encuestas obligatorias\n- Declaración IRS: USD 800\n\n **Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "llc_delaware_single": "- Costo estimado: USD 739\n- Prestigio legal a nivel internacional\n- Recomendado para startups, tecnología y negocios con socios\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "llc_delaware_multi": "- Costo estimado: USD 1400\n- Incluye cuenta bancaria y encuestas obligatorias\n- Declaración IRS: USD 800\n\n **Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "llc_wyoming_single": "- Costo estimado: USD 500\n- Privacidad y costos anuales bajos\n- Impuesto estatal: USD 62\n- Declaración IRS: USD 500\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "llc_wyoming_multi": "- Costo estimado: USD 800\n- Agente registrado: USD 100\n- Impuesto estatal: USD 62\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "impuestos_single": "- Formulario 5472 + libro contable obligatorio\n- Si hubo ingresos, presentar Schedule C\n- Multa por no presentar: hasta USD 25.000\n- Tiempo estimado: 3 a 5 días hábiles\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "impuestos_multi": "- Formulario 1065 obligatorio\n- Cada socio debe recibir un K-1\n- W-8BEN-E si los socios son extranjeros\n- Multa por no presentar: USD 210 por socio por mes\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min",
    "cuenta_sin_llc": "- Requiere LLC + EIN\n- Podemos ayudarte a abrir cuenta en Mercury, Relay o bancos físicos\n- Si no tenés estructura, sugerimos abrir primero una LLC\n\n**Agendá tu llamada sin costo con:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min"
}



if intencion == "¿Quiénes somos?":
    st.subheader("¿Quiénes somos en FINANCERS?")
    st.markdown("""
Somos un equipo contable-financiero offshore en Estados Unidos y Argentina que colabora con inversores, empresas tecnológicas y estudios contables de Latinoamérica.

Contamos con **más de 1000 clientes** y un equipo de **15 profesionales especializados**, distribuidos entre **Argentina, Estados Unidos y Alemania**, enfocados en cada etapa del proceso: formación de LLCs, cumplimiento fiscal, y apertura de cuentas bancarias.

Nos especializamos en ofrecer soluciones para que puedas gestionar tu contabilidad en Estados Unidos de manera segura y confiable, hablando tu mismo idioma y permitiéndote trabajar con tranquilidad.
""")




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
        st.markdown("👉 [Agendá tu llamada sin costo con]:** Matías Gasser https://calendly.com/mgasser-ueq/30min o con el Cr. Mira Salas https://calendly.com/crmirasalas/30min")

    elif conocimiento == "Sí":
        estado = st.selectbox("¿En qué estado querés abrirla?", ["", "Florida", "Delaware", "New Mexico", "Wyoming"])
        tipo = st.selectbox("¿La manejarás solo o con otros socios?", ["", "Single Member", "Multi Member"])

        if estado and tipo:
            key = f"llc_{estado.lower().replace(' ', '_')}_{tipo.lower().split()[0]}"
            
            if key in respuestas:
                st.markdown("### Resultado")
                st.markdown(respuestas[key])

                # PDF descargables según estado y tipo (solo si coincide)
                pdf_links = {
                    "llc_florida_single": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/LLC%20-%20Single%20Member%20Florida.pdf",
                    "llc_new_mexico_single": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/LLC%20-%20Single%20Member%20New%20Mexico.pdf",
                    "llc_delaware_single": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/LLC%20-%20Delaware.pdf"
                }
                # Equivalencias MM con su PDF de SM y texto aclaratorio
                equivalentes_mm = {
                    "llc_florida_multi": ("llc_florida_single", "La estructura Multi Member requiere formulario 1065 y K-1 para cada socio. La declaración federal cuesta 800 USD. Recomendamos esta opción si habrá cuentas compartidas, más de un responsable o capital conjunto."),
                    "llc_new_mexico_multi": ("llc_new_mexico_single", "Como Multi Member, el costo estimado sube a 700 USD e incluye cuenta bancaria. La declaración anual cuesta 800 USD e implica emitir un K-1 por cada socio."),
                    "llc_delaware_multi": ("llc_delaware_single", "La versión Multi Member cuesta 1400 USD e incluye BOI, BE-13 y cuenta bancaria. La declaración ante IRS cuesta 800 USD. Ideal si vas a compartir responsabilidades o ingresos.")
                }

                if key in pdf_links:
                    st.markdown(f"📄 [Descargar PDF informativo]({pdf_links[key]})")
                elif key in equivalentes_mm:
                    sm_key, extra = equivalentes_mm[key]
                    st.markdown(f"📄 [Descargar PDF informativo (versión Single Member)]({pdf_links[sm_key]})")
                    st.info(extra)
                

# PDFs de presupuestos para declaración de impuestos
pdf_impuestos = {
    "florida_single": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20SM%20-%20Florida%20(FL)%20-FINANCERS.pptx.pdf",
    "florida_multi": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20MM%20-%20Florida%20(FL)%20-FINANCERS.pptx.pdf",
    "new_mexico_single": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20SM%20-%20New%20Mexico%20(NM)%20-FINANCERS.pptx.pdf",
    "new_mexico_multi": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20MM%20-%20New%20Mexico%20(NM)%20-FINANCERS.pptx.pdf",
    "delaware_single": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20SM%20-%20Delaware%20(DE)%20-FINANCERS.pptx.pdf",
    "delaware_multi": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20MM%20-%20Delaware%20(DE)%20-FINANCERS.pptx.pdf",
    "wyoming_single": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20SM%20-%20Wyoming%20(WY)%20-FINANCERS.pptx.pdf",
    "wyoming_multi": "https://raw.githubusercontent.com/juaniroa1/financers-bot/main/pdfs/Presupuesto%20MM%20-%20Wyoming%20(WY)%20-FINANCERS.pptx.pdf"
}
if intencion == "Declarar impuestos":
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
            key_pdf = f"{estado.lower().replace(' ', '_')}_{tipo.lower().split()[0]}"
            if key_pdf in pdf_impuestos:
                st.markdown(f"📄 [Descargar presupuesto detallado en PDF]({pdf_impuestos[key_pdf]})")
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

            st.markdown("**Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)")

    else:
        st.warning("Para declarar impuestos primero debés tener una LLC. Podemos ayudarte con la apertura.")

if intencion == "Abrir una cuenta bancaria":
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

if intencion == "Enviar una consulta personalizada":
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

if intencion == "No sé por dónde empezar":
    st.subheader("¡Empecemos por lo básico!")

    opciones = {
        "Quiero más información o no sé bien qué necesito": """Hola, buen día.
Soy Juan Cruz de FINANCERS, un gusto.

Te cuento: ayudamos a emprendedores e inversores latinos a operar legalmente en EE.UU.

¿Tenés pensado abrir una empresa, declarar impuestos o necesitás ayuda con una cuenta bancaria?
Con una mínima info ya te puedo orientar.""",

        "Vi algo sobre crear una empresa": """Genial.
¿Tenés pensado armarla solo o con socios? Eso define si sería una LLC Single Member o Multi Member.

Y si ya sabés en qué estado te interesa (New Mexico, Florida, Delaware), te paso el presupuesto detallado y ventajas de cada uno.""",

        "Estoy en otro país, ¿puedo abrir una cuenta o empresa?": """Sí, sin problema. No necesitás vivir en EE.UU.

Te ayudamos a abrir una empresa 100% online desde tu país, obtener el EIN, y abrir la cuenta bancaria con bancos como Mercury o Relay.

¿Querés que te pase los requisitos y el presupuesto estimado?"""
    }

    seleccion = st.selectbox("Elegí una pregunta inicial", list(opciones.keys()))
    st.markdown("### Respuesta sugerida")
    st.markdown(opciones[seleccion])


if intencion == "Preguntas frecuentes":
    st.subheader("Preguntas frecuentes")

    categorias = {
        "Apertura de LLC": [
            ("¿En qué estado me conviene crear la LLC?",
             """Depende del objetivo de tu negocio:

- **New Mexico** es ideal si buscás privacidad, bajo costo y no necesitás una imagen corporativa reconocida.
- **Florida** es excelente si vas a invertir en inmuebles, operar con cuentas bancarias locales o necesitás tener presencia en un estado comercialmente activo.
- **Delaware** es el más prestigioso desde el punto de vista legal. Muy recomendado para startups, empresas tecnológicas o si vas a levantar capital o tener inversores.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Qué incluye el servicio de apertura?",
             """Nuestro servicio incluye:

- Registro legal de la LLC ante el estado correspondiente
- Obtención del EIN (número de identificación fiscal) ante el IRS
- Alta del agente registrado (Registered Agent)
- Operating Agreement
- Presentación del BOI (Beneficial Ownership Information)
- Asistencia para apertura de cuenta bancaria
- Asesoría en español durante todo el proceso

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Qué significa ser Single Member o Multi Member?",
             """- **Single Member (SM):** una sola persona como titular. Declaración más simple (formulario 5472). Menor costo de mantenimiento.
- **Multi Member (MM):** dos o más socios. Requiere presentación del formulario 1065 + K-1. Útil para cuentas compartidas o responsabilidades divididas.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿La LLC permite recibir pagos internacionales?",
             """Sí. Con tu LLC podés recibir pagos desde cualquier parte del mundo. Plataformas como Stripe, Wise, Payoneer, Deel, Binance, etc. son compatibles.

También podés emitir facturas a clientes internacionales y operar como proveedor global.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Qué costo tiene abrir una LLC?",
             """Depende del estado y tipo de estructura:

- New Mexico SM: desde USD 700
- Florida SM: USD 1000 (más RA y Sunbiz)
- Delaware SM: USD 1300 (más Franchise Tax de USD 300)

Todos incluyen la cuenta bancaria y presentación BOI.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
""")
        ],
        "Estate Tax y estructuras offshore": [
            ("¿Qué es el Estate Tax y cuándo aplica?",
             """El Estate Tax es un impuesto a la herencia que puede alcanzar hasta el 40% sobre el valor de los activos que un extranjero posea directamente en EE.UU., como propiedades a nombre de una LLC. Si el titular fallece sin una estructura que lo proteja, sus herederos podrían enfrentar esta carga fiscal. Para evitarlo, se recomienda crear una sociedad offshore (como una BVI) que sea la propietaria de la LLC.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Qué tipo de offshore recomiendan?",
             """La estructura más utilizada por nuestros clientes es una sociedad en las Islas Vírgenes Británicas (BVI). Esta entidad es confidencial, ágil de constituir, y permite que vos seas el beneficiario final sin figurar directamente en EE.UU. Es ideal para propietarios de inmuebles o cuentas bancarias que quieren reducir riesgos legales y fiscales.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Puedo usar una offshore para proteger activos?",
             """Sí. Muchas veces se crea una BVI como holding que controla la LLC estadounidense. Esto no sólo evita el Estate Tax, sino que brinda una capa adicional de privacidad y planificación fiscal. Es legal, transparente, y muy común en estructuras de no residentes.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Es obligatorio usar offshore si tengo propiedades?",
             """No es obligatorio, pero sí altamente recomendable si el valor de los activos supera los USD 60.000. Por encima de ese umbral, el IRS podría aplicar el Estate Tax. Si querés evitar riesgos a largo plazo, es mejor prevenir con una estructura adecuada.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿La offshore paga impuestos?",
             """No. Una sociedad offshore como BVI no paga impuestos en su país de incorporación ni en EE.UU. si no opera directamente allí. Su función es de control y tenencia, no de operación directa.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
""")
        ],
        
        "Declaración de impuestos": [
            ("¿Debo declarar si la LLC no tuvo movimientos?",
             """Sí. Toda LLC con EIN está obligada a presentar declaración anual.

- SM: formularios 1120 + 5472
- MM: formulario 1065 + K-1 para cada socio

No declarar puede implicar multas de hasta USD 25.000.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Cuál es el costo de la declaración anual?",
             """- SM: USD 500
- MM: USD 800

Además, sumá:
- RA: USD 100
- Estado: FL (139), DE (300), NM (0), WY (62)

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Qué es el RA, Sunbiz o Franchise Tax?",
             """- **RA:** agente registrado (USD 100/año)
- **Sunbiz:** registro estatal obligatorio en Florida (USD 139)
- **Franchise Tax:** impuesto anual de Delaware (USD 300)

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Puedo pagarme un sueldo desde la LLC?",
             """Si no sos residente fiscal en EE.UU., podés hacer transferencias personales como retiro de utilidades.

Si sos residente o tenés actividad física allá, necesitás registrarte como empleador.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Cómo declaro en Argentina los ingresos desde la LLC?",
             """Se declaran como ingresos de fuente extranjera en el Impuesto a las Ganancias.

También pueden estar alcanzados por Bienes Personales. Consultá con tu contador local.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
""")
        ],
        "Cuenta bancaria": [
            ("¿Qué banco recomiendan?",
             """Usamos Relay y Mercury Financial como primera opción:

- 100% online
- Multiusuario
- Recibe pagos de Stripe, Wise, Deel, Payoneer
- No requiere residencia en EE.UU.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Puedo abrir una cuenta como extranjero?",
             """Sí. No necesitás visa ni estar en EE.UU.

Solo necesitás:
- LLC activa
- EIN
- Documentación societaria
- Pasaporte vigente

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Qué necesito para abrir la cuenta?",
             """- LLC registrada
- EIN emitido
- Articles of Organization + Operating Agreement
- Pasaporte
- Servicio a tu nombre

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Puedo transferir fondos desde Argentina u otros países?",
             """Sí. Relay permite recibir transferencias SWIFT desde el exterior y también operar con Wise, Payoneer, etc.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
"""),
            ("¿Qué pasa si no puedo completar el onboarding?",
             """Nuestro equipo te ayuda a corregir errores y reintentar. Si Relay no aprueba, usamos Mercury, IFB u otras opciones.

👉 **Agendá tu llamada sin costo con:** [Matías Gasser](https://calendly.com/mgasser-ueq/30min) o con el Cr. Mira Salas [aquí](https://calendly.com/crmirasalas/30min)
""")
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

# Nota legal al pie
st.markdown("---")
st.markdown("**Importante:** Si no estás más de 183 días en EE.UU., no generás ingresos conectados (ECI) ni ingresos de fuente estadounidense, no debés tributar. Aun así, debés presentar tu declaración anual ante el IRS.")
st.markdown("**Si tenés inmuebles o empleados en EE.UU.**, deberías tributar y lo recomendable sería una C-Corp (tasa fija del 21%).")

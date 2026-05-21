import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import rastreador_aprovados as backend

# Inicialização de sessão
if "df_resultado_conferencia" not in st.session_state:
    st.session_state.df_resultado_conferencia = None

# Funções de callback
def realiza_conferencia():
    if arquivo_lista_alunos and arquivo_lista_vestibular:
        with st.spinner('Lendo arquivos e cruzando dados... Isso pode levar alguns segundos.'):
            st.session_state.df_resultado_conferencia = backend.processar_conferencia(
                arquivo_lista_alunos,
                arquivo_lista_vestibular,
                st.session_state.opcao == "Nome + CPF"
            )
    else:
        st.error("Por favor, faça o upload dos dois arquivos.")

# Configuração da página
st.set_page_config(
    page_title="Rastreador de Aprovados",
    page_icon="🦉",
    layout="centered"
)

# Estilização CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

/* Fonte global */
html, body, [data-testid="stAppViewContainer"], .stApp {
  font-family: 'Poppins', sans-serif !important;
}

/* Título fora do card */
.titulo { 
    font-weight: 800; 
    font-size: 28px !important; 
    margin: 0; 
    color: inherit; 
    white-space: nowrap;
}

/* Garantir que labels e textos gerais sejam brancos dentro do card */
[data-testid="stWidgetLabel"] p, 
[data-testid="stMarkdownContainer"] p, 
[data-testid="stRadio"] label {
    color: white !important;
}

/* Botão principal */
div.stButton > button {
  background-color: #ef7b17 !important;
  color: white !important;
  border-radius: 8px !important;
  border: none !important;
}

[data-testid="stFileUploader"] div,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] p {
    color: white !important;
}

[data-testid="stFileUploaderDropzone"] {
    background-color: rgba(255, 255, 255, 0.1) !important;
    border: 1px dashed rgba(255, 255, 255, 0.6) !important;
}

[data-testid="stFileUploader"] button {
    color: white !important;
    border-color: white !important;
    background-color: transparent !important;
}
[data-testid="stFileUploader"] button:hover {
    background-color: rgba(255, 255, 255, 0.1) !important;
    border-color: #ef7b17 !important;
    color: #ef7b17 !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] > div > span,
[data-testid="stFileUploaderDropzoneInstructions"] > div > small {
    display: none;
}
[data-testid="stFileUploaderDropzoneInstructions"] > div::after {
   content: "Solte seu arquivo aqui";
   display: block;
   font-size: 16px;
   margin-bottom: 5px;
   color: white !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] > div::before {
   content: "Limite de 1GB • CSV, XLSX, PDF, TXT";
   display: block;
   font-size: 12px;
   color: #ddd !important;
   margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# Cabeçalho
col_img, col_titulo = st.columns([1, 9], vertical_alignment="center")
with col_img:
   st.image("logo.png", width=120)
with col_titulo:   
   st.markdown("<h2 class='titulo'> Rastreador de<br>Aprovados</h2>", unsafe_allow_html=True)

# Área principal do app
with stylable_container(
    key="meu_card",
    css_styles="""
        {
            background-color: #15355B; 
            border-radius: 15px; 
            padding: 30px; 
            color: white !important;
        }
    """
):
    st.markdown('<h3 style="color:white; margin-top:0;">Conferência de listas</h3>', unsafe_allow_html=True)
    st.info("Agora aceita arquivos PDF e TXT diretamente! O sistema buscará o nome dos alunos dentro do arquivo da lista oficial.")

    # Opções de método
    st.radio(
        "Método de validação:",
        ["Nome completo", "Nome + CPF"],
        horizontal=True,
        key="opcao",
        help="Se escolher nome + CPF, o sistema procurará o nome do aluno e verificará se algum fragmento do CPF dele está próximo no texto."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p style="color:white; font-weight:bold;">1. Alunos do cursinho</p>', unsafe_allow_html=True)
        arquivo_lista_alunos = st.file_uploader(
            "Upload da lista de alunos", 
            type=["csv", "xlsx"], 
            key="a1", 
            label_visibility="collapsed"
        )

    with col2:
        st.markdown('<p style="color:white; font-weight:bold;">2. Lista oficial</p>', unsafe_allow_html=True)
        arquivo_lista_vestibular = st.file_uploader(
            "Upload da lista oficial", 
            type=["csv", "xlsx", "pdf", "txt"], 
            key="a2", 
            label_visibility="collapsed"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Botão de busca
    st.button("Buscar", on_click=realiza_conferencia, use_container_width=True)

    # Exibição dos resultados
    if st.session_state.df_resultado_conferencia is not None:
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("### Resultado da análise:")
        st.dataframe(st.session_state.df_resultado_conferencia, use_container_width=True)
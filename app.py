import streamlit as st
import pandas as pd
import re
from io import BytesIO

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Anonimizador RH", page_icon="🛡️")

st.title("🛡️ Anonimizador de Dados de RH")
st.markdown("""
Esta ferramenta foi desenvolvida para garantir a **Segurança Jurídica (LGPD)** no manuseio de dados.
Ela mascara automaticamente dados sensíveis (CPF e Email) de planilhas Excel.
""")

# --- FUNÇÕES DE LÓGICA (O mesmo cérebro do seu script anterior) ---
def mascarar_cpf(cpf):
    cpf_str = str(cpf)
    if cpf_str == 'nan': return "N/A"
    cpf_limpo = re.sub(r'[^0-9]', '', cpf_str)
    cpf_cheio = cpf_limpo.zfill(11)
    return cpf_cheio[:3] + ".***.***-**"

def mascarar_email(email):
    email_str = str(email)
    if email_str == 'nan' or '@' not in email_str: return "N/A"
    try:
        partes = email_str.split('@')
        usuario = partes[0]
        dominio = partes[1]
        novo_usuario = usuario[0] + "****" if len(usuario) > 1 else "****"
        return f"{novo_usuario}@{dominio}"
    except:
        return "erro_formatacao"

# --- INTERFACE DE UPLOAD ---
# A área onde o usuário arrasta o arquivo
arquivo = st.file_uploader("Carregue sua planilha (.xlsx)", type=["xlsx"])

if arquivo is not None:
    # Lê o arquivo direto da memória RAM (Seguro e Rápido)
    df = pd.read_excel(arquivo)
    
    st.success(f"Arquivo carregado! {len(df)} registros encontrados.")
    

    # --- BOTÃO DE AÇÃO ---
    if st.button("🔒 Anonimizar Dados Agora", type="primary"):
        
        colunas_tratadas = []
        
        # Processa CPF se existir
        if 'CPF' in df.columns:
            df['CPF'] = df['CPF'].apply(mascarar_cpf)
            colunas_tratadas.append("CPF")
            
        # Processa Email se existir
        if 'Email' in df.columns:
            df['Email'] = df['Email'].apply(mascarar_email)
            colunas_tratadas.append("Email")
            
        if colunas_tratadas:
            st.balloons() # Efeito visual de sucesso!
            st.success(f"Feito! Colunas anonimizadas: {', '.join(colunas_tratadas)}")
            
            st.subheader("Resultado (Prévia):")
            st.dataframe(df.head())
            
            # --- DOWNLOAD ---
            # Prepara o arquivo para baixar sem salvar no disco
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False)
                
            st.download_button(
                label="📥 Baixar Planilha Segura (.xlsx)",
                data=buffer,
                file_name="dados_rh_protegidos.xlsx",
                mime="application/vnd.ms-excel"
            )
        else:
            st.error("⚠️ Atenção: Não encontrei as colunas 'CPF' ou 'Email' na sua planilha. Verifique o cabeçalho.")
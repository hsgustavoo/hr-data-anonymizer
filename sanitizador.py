import pandas as pd
import re
import os

print("--- 🚀 Iniciando o processamento ---")

# --- 1. CONFIGURAÇÃO DE CAMINHOS ---
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_entrada = os.path.join(diretorio_script, "dados", "dados_rh.xlsx")
caminho_saida = os.path.join(diretorio_script, "dados", "dados_publicos.xlsx")

# --- 2. CARREGAMENTO ---
try:
    print(f"📂 Lendo arquivo: {caminho_entrada}")
    df = pd.read_excel(caminho_entrada)
    print(f"✅ Arquivo carregado! {len(df)} registros encontrados.")
except FileNotFoundError:
    print("❌ ERRO: Arquivo 'dados_rh.xlsx' não encontrado na pasta 'dados/'.")
    exit()

# --- 3. FUNÇÕES DE ANONIMIZAÇÃO ---

def mascarar_cpf(cpf):
    cpf_str = str(cpf)
    if cpf_str == 'nan': return "N/A"
    
    # Deixa só números
    cpf_limpo = re.sub(r'[^0-9]', '', cpf_str)
    
    # Garante 11 dígitos
    cpf_cheio = cpf_limpo.zfill(11)
    
    # Máscara: 123.***.***-**
    return cpf_cheio[:3] + ".***.***-**"

def mascarar_email(email):
    email_str = str(email)
    
    # Se estiver vazio ou não tiver @, retorna como inválido ou N/A
    if email_str == 'nan' or '@' not in email_str:
        return "N/A"
    
    try:
        # Quebra o email em duas partes: antes e depois do @
        # Ex: gustavo @ linx.com.br
        partes = email_str.split('@')
        usuario = partes[0]
        dominio = partes[1]
        
        # Pega a primeira letra do usuário e adiciona ***
        # Se o usuário for muito curto (ex: a@b.com), mascara tudo
        if len(usuario) > 1:
            novo_usuario = usuario[0] + "****"
        else:
            novo_usuario = "****"
            
        return f"{novo_usuario}@{dominio}"
        
    except Exception:
        return "erro_formatacao"

print("--- 🎭 Aplicando máscaras (CPF e Email)... ---")

# --- 4. APLICAÇÃO ---
try:
    # Aplica no CPF
    if 'CPF' in df.columns:
        df['CPF_Anonimizado'] = df['CPF'].apply(mascarar_cpf)
        df = df.drop(columns=['CPF'])
    else:
        print("⚠️ Aviso: Coluna 'CPF' não encontrada.")

    # Aplica no Email (Nova Funcionalidade)
    if 'Email' in df.columns:
        df['Email_Anonimizado'] = df['Email'].apply(mascarar_email)
        df = df.drop(columns=['Email']) # Remove o email original
    else:
        print("⚠️ Aviso: Coluna 'Email' não encontrada.")

    # --- 5. SALVAMENTO ---
    df.to_excel(caminho_saida, index=False)
    print(f"✅ SUCESSO! Arquivo gerado em: {caminho_saida}")

except Exception as e:
    print(f"❌ Ocorreu um erro inesperado: {e}")
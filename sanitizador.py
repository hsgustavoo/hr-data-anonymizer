import pandas as pd
import re  # Para limpeza de caracteres (Regex)
import os  # Para lidar com caminhos de pastas no Windows

print("--- 🚀 Iniciando o processamento ---")

# --- 1. CONFIGURAÇÃO INTELIGENTE DE CAMINHOS ---
# Descobre onde este script (sanitizador.py) está salvo no seu PC
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Monta o caminho exato para a pasta 'dados' baseada na posição do script
# Isso resolve o erro de "File Not Found" mesmo se o terminal estiver na pasta errada
caminho_entrada = os.path.join(diretorio_script, "dados", "dados_rh.xlsx")
caminho_saida = os.path.join(diretorio_script, "dados", "dados_publicos.xlsx")

# --- 2. CARREGAMENTO DO ARQUIVO ---
try:
    print(f"📂 Procurando arquivo em: {caminho_entrada}")
    df = pd.read_excel(caminho_entrada)
    print(f"✅ Arquivo carregado! Encontrei {len(df)} colaboradores.")

except FileNotFoundError:
    print("\n❌ ERRO CRÍTICO: O arquivo não foi encontrado!")
    print(f"Certifique-se que 'dados_rh.xlsx' está dentro da pasta: {os.path.join(diretorio_script, 'dados')}")
    exit() # Para o código aqui

# --- 3. FUNÇÃO DE ANONIMIZAÇÃO ---
def mascarar_cpf(cpf):
    # Converte para texto
    cpf_str = str(cpf)
    
    # TRATAMENTO DE ERRO: Se a célula estiver vazia (nan), retorna N/A
    if cpf_str == 'nan':
        return "N/A"
    
    # LIMPEZA: Remove tudo que NÃO for número (pontos, traços, espaços)
    # Regex: [^0-9] significa "qualquer coisa que não seja 0 a 9"
    cpf_limpo = re.sub(r'[^0-9]', '', cpf_str)
    
    # Garante 11 dígitos com zeros à esquerda
    cpf_cheio = cpf_limpo.zfill(11)
    
    # Aplica a máscara (Ex: 123.***.***-**)
    return cpf_cheio[:3] + ".***.***-**"

print("--- 🎭 Anonimizando CPFs... ---")

# --- 4. APLICAÇÃO E SALVAMENTO ---
try:
    # Aplica a função linha por linha
    df['CPF_Anonimizado'] = df['CPF'].apply(mascarar_cpf)
    
    # Remove a coluna original (Perigosa)
    df = df.drop(columns=['CPF'])
    
    # Salva o resultado no caminho de saída configurado lá em cima
    df.to_excel(caminho_saida, index=False)
    
    print(f"\n✅ SUCESSO! Arquivo salvo em: {caminho_saida}")

except KeyError:
    print("\n❌ ERRO NA PLANILHA: Não achei a coluna 'CPF'.")
    print("Verifique se no Excel a coluna está escrita como 'cpf', 'C.P.F' ou tem espaços extras.")
except Exception as e:
    print(f"\n❌ Erro inesperado: {e}")
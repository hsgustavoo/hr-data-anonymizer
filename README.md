# 🛡️ Pipeline de Anonimização de Dados de RH (LGPD)

> "Segurança Jurídica & Automação no tratamento de dados sensíveis."

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)
![Compliance](https://img.shields.io/badge/Foco-LGPD-green?style=for-the-badge)

## 📄 Sobre o Projeto
Este projeto é uma ferramenta agnóstica desenvolvida para **sanitizar planilhas de RH** contendo dados sensíveis (PII - *Personally Identifiable Information*) antes de qualquer compartilhamento externo ou uso em ambientes de teste.

O objetivo é eliminar o erro humano e garantir conformidade com a **LGPD (Lei Geral de Proteção de Dados)**, automatizando o mascaramento de informações críticas.

## ⚙️ Funcionalidades Atuais
- ✅ **Leitura Inteligente:** Identifica e carrega arquivos `.xlsx` automaticamente.
- ✅ **Mascaramento de CPF:** Aplica máscara parcial (`123.***.***-**`) e remove pontuações irregulares.
- ✅ **Validação de Dados:** Tratamento de células vazias ou corrompidas para evitar quebra do script.
- ✅ **Proteção de Fonte:** Gera um novo arquivo (`dados_publicos.xlsx`) preservando o arquivo original intacto.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12**
* **Pandas:** Manipulação de DataFrames e leitura de Excel.
* **Regex (Re):** Limpeza e padronização de strings.
* **OS:** Gerenciamento agnóstico de caminhos de arquivos (compatível com Windows/Linux).

## 🚀 Como Executar
1. Clone este repositório:
```bash
git clone [https://github.com/hsgustavoo/anonimizador-de-dados-de-rh.git](https://github.com/hsgustavoo/anonimizador-de-dados-de-rh.git)

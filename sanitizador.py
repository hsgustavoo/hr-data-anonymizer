import pandas as pd
#Python, chama o especialista em Excel e Tabelas (Pandas). E para eu não ter que ficar escrevendo 'pandas' toda hora, vou chamar ele pelo apelido de 'pd'.

df = pd.read_excel("dados_rh.xlsx")
#Ei, Pandas, lê esse arquivo Excel chamado "dados_rh.xlsx" que está na pasta e guarda ele na memória do computador.
#A sigla 'df' é uma abreviação comum para 'DataFrame'. Imagine que essa sigla é a planilha aberta voando na memória RAM do seu computador. Tudo que fizermos, faremos no 'df', sem estragar o arquivo original.

def mascarar_cpf(cpf):
    cpf_str = str(cpf)
    cpf_str = cpf_str.zfill(11)
    #"Zero Fill" Preencher com zeros
    #O Excel tem uma mania feia, ele acha que CPF é número matemático. Se o CPF começar com zero, ele corta o zero. Então, para garantir que todo CPF tenha 11 dígitos, o comando zfill(11) adiciona zeros à esquerda, se necessário.
    return cpf_str[:3] + ".***.***-**"
#def significa "atenção, vou definir uma regra chamada mascarar_cpf".
#cpf_str = str(cpf) "Pega o CPF que você recebeu e transforme ele em texto (string), pra eu poder cortar ele em pedaços."
#"cpf_str[:3}:"Pega só os três primeiros números do CPF.
#+ ... :"Cola esse final cheio de asteriscos no lugar do resto".

df['CPF_Anonimizado'] = df['CPF'].apply(mascarar_cpf)
#df{'CPF'}:"Olha só para a coluna CPF".
#.apply(mascarar_cpf): Aplicar aquela regra que eu ensinei em CADA UMA das linhas, uma por uma, automaticamente".
#df['CPF_Anonimizado'] = : "Guarda o resultado numa coluna nova chamada 'CPF_Anonimizado'".

#Aqui está o comando que remove a coluna original de CPF, que não queremos mais.
#O comando .drop joga fora a coluna CPF
#O axis=1 avisa que é para procurar ha horizontal (coluna), não linhas.
df = df.drop(columns=['CPF'])

df.to_excel("dados_publicos.xlsx", index=False)
#O que significa: estagiário, pega essa planilha que está na memória (df), com as alterações que fizemos, e salva num arquivo novo chamado 'dados_publicos.xlsx'

print("Sucesso! A coluna 'CPF' original foi destruída e o arquivo está seguro.")
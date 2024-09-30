'''
ANNY CAROLINA - RM:98295
DEBORA AMARAL - RM:550412
LEVY JUNIOR - RM:98655
LÍVIA NAMBA - RM:97819
LUANA CABEZAOLIAS - RM:99320
'''

# importando bibliotecas
import numpy as np
import pandas as pd
import time

# função para o login do usuário
def login(username, password):
    # simula o login do usuário (pode ser integrado com um banco de dados real, mas por enquanto deixamos um único usuário e senha para uma breve simulação)
    if username == "usuario" and password == "1234":
        print("Login bem-sucedido! Bem-vindo ao LaparoVR.")
        return True
    else:
        print("Falha na autenticação. Verifique seu login e senha.")
        return False

# função para iniciar o ambiente de simulação VR
def iniciar_simulacao():
    print("Iniciando simulação VR de cirurgia laparoscópica...")
    # equipamentos e ferramentas simuladas
    ferramentas = ["Pinça", "Câmera", "Bisturi"]
    print(f"Ferramentas disponíveis: {ferramentas}")
    time.sleep(2)

# função para coletar dados durante o procedimento (tempo, precisão, erros)
def coletar_dados_simulacao():
    tempo_execucao = np.random.randint(300, 600)  # tempo entre 5 a 10 minutos
    precisao = np.random.randint(70, 100)  # precisão entre 70% a 100%
    erros = np.random.randint(0, 5)  # erros cometidos (0 a 5)
    return tempo_execucao, precisao, erros

# função para avaliar o desempenho e fornecer feedback
def avaliar_desempenho(dados):
    print("\n--- Relatório de Desempenho ---")
    print(f"Tempo Total: {dados[0]} segundos")
    print(f"Pontuação de Precisão: {dados[1]}%")
    print(f"Erros Cometidos: {dados[2]}")
    if dados[1] >= 85:
        print("Desempenho satisfatório. Continue praticando!")
    else:
        print("Atenção: É necessário melhorar sua precisão.")

# função para armazenar os resultados em um DataFrame
def armazenar_resultados(tabela, dados):
    # adiciona os resultados à tabela (DataFrame)
    nova_linha = pd.DataFrame([dados], columns=['Tempo de Execução (segundos)', 'Precisão (%)', 'Erros Cometidos'])
    tabela = pd.concat([tabela, nova_linha], ignore_index=True) 
    return tabela

# função para simular a visualização do progresso no portal
def ver_progresso(tabela):
    print("\n--- Histórico de Treinamento ---")
    print(tabela)

# função para o menu principal
def menu_principal(tabela_resultados):
    while True:
        print("\nPainel de Controle:")
        print("1. Iniciar Treinamento")
        print("2. Ver Progresso")
        print("3. Sair")
        
        opcao = input("Selecione uma opção: ")
        
        if opcao == '1':
            iniciar_simulacao()
            dados = coletar_dados_simulacao()
           
            # avalia o desempenho do usuário
            avaliar_desempenho(dados)
           
            # armazena os resultados
            tabela_resultados = armazenar_resultados(tabela_resultados, dados)
        
        elif opcao == '2':
            ver_progresso(tabela_resultados)
        elif opcao == '3':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# função principal do sistema
def main():
    # simula o banco de dados de resultados
    tabela_resultados = pd.DataFrame(columns=['Tempo de Execução (segundos)', 'Precisão (%)', 'Erros Cometidos'])
   
    while True:  # loop para login
        username = input("Digite seu login: ")
        password = input("Digite sua senha: ")
       
        if login(username, password):
            menu_principal(tabela_resultados)
            break 
        else:
            print("Acesso negado. Tente novamente.")

if __name__ == "__main__":
    main()

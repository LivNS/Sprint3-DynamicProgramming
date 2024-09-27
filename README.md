# 🕹LaparoVR🎮

## 📌Introdução

O **LaparoVR** é uma plataforma inovadora de treinamento em laparoscopia que utiliza tecnologia de realidade virtual para proporcionar uma experiência de aprendizado imersiva e interativa para estudantes de medicina e profissionais de saúde. O objetivo do projeto é revolucionar o treinamento de habilidades cirúrgicas, permitindo que os usuários pratiquem e aperfeiçoem técnicas laparoscópicas em um ambiente virtual realista e seguro.

## 🎯Objetivos do Projeto

- Proporcionar um ambiente de simulação cirúrgica realista.
- Facilitar a aprendizagem de técnicas laparoscópicas.
- Oferecer feedback em tempo real sobre o desempenho dos usuários.
- Armazenar e analisar dados de desempenho para melhoria contínua.

## 🛠Funcionalidades Principais

1. **Ambiente Virtual de Simulação**: 
   - Simulação de uma sala de cirurgia com gráficos de alta qualidade e física realista.
   - Interação intuitiva com equipamentos e ferramentas laparoscópicas.

2. **Tutorial Interativo**: 
   - Orientações passo a passo para a realização de procedimentos cirúrgicos.
   - Feedback instantâneo sobre a execução das técnicas.

3. **Personalização do Treinamento**: 
   - Opções para ajustar o nível de dificuldade e focar em áreas específicas de prática.

4. **Interface do Usuário Intuitiva**: 
   - Navegação fácil e acessível dentro do ambiente virtual.
   - Painéis e menus claros para controle e configuração.

5. **Armazenamento de Dados**: 
   - Coleta de dados de desempenho durante as simulações, incluindo tempo de execução, precisão e erros cometidos.
   - Visualização do histórico de treinamento.
  
## ✨Detalhes do Código

O código do LaparoVR foi projetado para simular um ambiente de treinamento em laparoscopia utilizando uma interface interativa. Abaixo estão os principais componentes e funcionalidades implementadas:

### 1. **Estrutura do Código**

O código é estruturado em várias funções que permitem modularidade e fácil manutenção. As principais funções são:

- **login(username, password)**: 
  - Simula o processo de login do usuário. Verifica se o nome de usuário e a senha estão corretos. Se o login for bem-sucedido, retorna `True`; caso contrário, retorna `False`.
  - Para logar é necessário colocar o User(sendo esse: 'usuario') e a senha(1234).

- **iniciar_simulacao()**: 
  - Inicializa o ambiente de simulação VR, apresentando as ferramentas disponíveis para a cirurgia laparoscópica.

- **coletar_dados_simulacao()**: 
  - Coleta dados aleatórios sobre a execução do procedimento, como tempo de execução, precisão e erros cometidos. Esses dados são gerados usando a biblioteca NumPy.

- **avaliar_desempenho(dados)**: 
  - Avalia o desempenho do usuário com base nos dados coletados. Fornece feedback sobre o tempo total, precisão e número de erros cometidos, e sugere melhorias se a precisão estiver abaixo de 85%.

- **armazenar_resultados(tabela, dados)**: 
  - Adiciona os dados de desempenho em um DataFrame do Pandas, permitindo que os resultados sejam armazenados e visualizados posteriormente.

- **ver_progresso(tabela)**: 
  - Exibe o histórico de treinamento do usuário, mostrando todos os dados coletados em simulações anteriores.

### 2. **Fluxo Principal do Sistema**

O fluxo do sistema é organizado da seguinte forma:

1. **Login**: O usuário é solicitado a inserir seu nome de usuário e senha. O sistema valida as credenciais e, se bem-sucedido, apresenta o painel de controle.

2. **Painel de Controle**: O usuário pode escolher entre três opções:
   - Iniciar Treinamento: O usuário inicia uma simulação cirúrgica.
   - Ver Progresso: O usuário visualiza o histórico de desempenho.
   - Sair: O usuário encerra o sistema.

3. **Início da Simulação**: Ao iniciar o treinamento, o sistema apresenta as ferramentas disponíveis e coleta dados durante a simulação.

4. **Avaliação de Desempenho**: Após a simulação, os dados coletados são avaliados, e um relatório de desempenho é gerado, fornecendo feedback ao usuário.

5. **Armazenamento e Visualização de Resultados**: Os resultados da simulação são armazenados em um DataFrame, que pode ser acessado a qualquer momento pelo usuário para revisar seu progresso.


## 💻Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para a implementação da lógica do sistema.
- **Pandas**: Biblioteca para manipulação e análise de dados, usada para armazenar e processar resultados.
- **NumPy**: Biblioteca para cálculos numéricos, utilizada para gerar dados aleatórios de simulação.
- **Realidade Virtual**: Tecnologias que permitem a simulação de ambientes 3D imersivos.

# 👩‍👩‍👧‍👧Contribuidores
- ANNY CAROLINA - RM:98295
- DEBORA AMARAL - RM:550412
- LEVY JUNIOR - RM:98655
- LÍVIA NAMBA - RM:97819
- LUANA CABEZAOLIAS - RM:99320


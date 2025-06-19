# --- Função 1: Verificar Umidade do Solo ---
# Função responsável por coletar e analisar os dados de umidade.
def verificar_umidade_solo():
    """
    Solicita o valor de umidade ao usuário, valida a entrada,
    analisa o valor e retorna uma string com o status e a recomendação.
    """
    # Imprime uma mensagem para o usuário, indicando qual processo está começando.
    print("\n--- Iniciando verificação de umidade do solo ---")
    
    # Loop infinito que só será quebrado quando uma entrada válida for fornecida.
    while True:
        # Coleta dados do usuário. Pede para que o operador insira o valor da umidade.
        umidade_lida_str = input("Qual o valor de umidade do solo (%) fornecido pelo sensor? ")
        
        try:
            # Tenta converter a entrada (string) para um número de ponto flutuante (float).
            umidade_lida = float(umidade_lida_str)
            # Imprime um feedback para o usuário, confirmando o dado recebido e formatado.
            print(f"Feedback: A umidade registrada foi de {umidade_lida}%.")
            # Se a conversão for bem-sucedida, o loop é interrompido.
            break
        except ValueError:
            # Se a conversão falhar (ex: usuário digitou texto), esta mensagem é exibida.
            print("ERRO: Entrada inválida. Por favor, digite apenas números.")
            
    # Estrutura condicional que analisa o valor de umidade e retorna a string de status.
    if umidade_lida < 30:
        # Retorna a string de status para ser usada por outra função.
        return "Status: Solo SECO. Recomenda-se acionar a irrigação."
    elif 30 <= umidade_lida <= 70:
        # Retorna a string de status ideal.
        return "Status: Umidade IDEAL. Nenhuma ação necessária."
    else:
        # Retorna a string de status de solo encharcado.
        return "Status: Solo ENCHARCADO. Risco de afogamento da raiz. Suspender irrigação."

# --- Função 2: Analisar Nutrientes do Solo ---
# Função responsável por coletar e analisar os dados de nutrientes.
def analisar_nutrientes():
    """
    Solicita o nível de Nitrogênio (N) ao usuário, valida a entrada,
    analisa o valor e retorna uma string com o status e a recomendação.
    """
    # Imprime um cabeçalho para informar o usuário sobre a tarefa atual.
    print("\n--- Iniciando análise de nutrientes do solo ---")
    
    # Loop para garantir que a entrada do usuário seja um número válido.
    while True:
        # Coleta dados do usuário sobre o nível de Nitrogênio (em PPM).
        nivel_n_str = input("Qual o nível de Nitrogênio (N) no solo (em PPM)? ")
        try:
            # Tenta converter a string de entrada para um número float.
            nivel_n = float(nivel_n_str)
            # Fornece um feedback imediato ao usuário, confirmando o dado inserido.
            print(f"Feedback: O nível de Nitrogênio (N) registrado foi de {nivel_n} PPM.")
            # Sai do loop se a entrada for válida.
            break
        except ValueError:
            # Captura o erro se a entrada não for um número e pede para tentar novamente.
            print("ERRO: Entrada inválida. Por favor, digite apenas números.")

    # Estrutura condicional para avaliar o nível do nutriente e retornar a string de status.
    if nivel_n < 10:
        return "Status: Nível de Nitrogênio BAIXO. Recomenda-se aplicação de fertilizante nitrogenado."
    elif 10 <= nivel_n <= 30:
        return "Status: Nível de Nitrogênio IDEAL. Monitoramento contínuo recomendado."
    else:
        return "Status: Nível de Nitrogênio ALTO. Risco de toxicidade. Suspender adubação."

# --- Função 3: Gerar Relatório Simples ---
# Função que consolida os resultados e interage com o usuário sobre a ação final.
def gerar_relatorio_simples(status_umidade, status_nutriente):
    """
    Recebe os status de umidade e nutrientes, exibe um relatório consolidado
    e pergunta ao usuário qual ação tomar (salvar/enviar).
    """
    # Imprime um cabeçalho para a seção de relatório.
    print("\n--- Gerando Relatório de Status do Solo ---")
    # Exibe os resultados recebidos como parâmetros das outras funções.
    print(f"1. Análise de Umidade: {status_umidade}")
    print(f"2. Análise de Nutrientes: {status_nutriente}")
    print("\nResumo: O relatório consolidado está pronto.")
    
    # Coleta uma decisão do usuário sobre o que fazer com o relatório.
    acao_relatorio = input("O que deseja fazer com o relatório? (Digite 'salvar' ou 'enviar'): ")

    # Fornece um feedback com base na escolha do usuário, usando .lower() para ser flexível.
    if acao_relatorio.lower() == 'salvar':
        print(f"Feedback: Ação selecionada -> '{acao_relatorio}'. O relatório será salvo localmente no sistema.")
    elif acao_relatorio.lower() == 'enviar':
        print(f"Feedback: Ação selecionada -> '{acao_relatorio}'. O relatório será enviado para o email do gestor.")
    else:
        print(f"Feedback: Ação '{acao_relatorio}' não reconhecida.")

# --- Função Principal e Menu ---
# Função que controla a execução do programa e exibe o menu para o usuário.
def main():
    """
    Função principal que gerencia o menu interativo e o fluxo do programa.
    """
    # Loop principal do menu, continua executando até que o usuário escolha sair.
    while True:
        # Exibe as opções do menu para o usuário.
        print("\n========== SOFTWARE DE MANEJO DE SOLO ==========")
        print("1. Executar APENAS verificação de umidade")
        print("2. Executar APENAS análise de nutrientes")
        print("3. Executar ANÁLISE COMPLETA e gerar relatório")
        print("4. Sair do programa")
        
        # Coleta a escolha do usuário.
        escolha = input("Escolha uma opção: ")

        # Verifica a escolha do usuário e chama a função correspondente.
        if escolha == '1':
            # Chama a função de umidade e imprime o resultado retornado.
            resultado_umidade = verificar_umidade_solo()
            print(f"\nResultado da Análise: {resultado_umidade}")
        elif escolha == '2':
            # Chama a função de nutrientes e imprime o resultado retornado.
            resultado_nutrientes = analisar_nutrientes()
            print(f"\nResultado da Análise: {resultado_nutrientes}")
        elif escolha == '3':
            # Orquestra a execução completa: coleta, análise e relatório.
            # 1. Chama a função de umidade e armazena seu retorno.
            status_umidade = verificar_umidade_solo()
            # 2. Chama a função de nutrientes e armazena seu retorno.
            status_nutrientes = analisar_nutrientes()
            # 3. Chama a função de relatório passando os resultados reais obtidos.
            gerar_relatorio_simples(status_umidade, status_nutrientes)
        elif escolha == '4':
            # Encerra o programa.
            print("\nEncerrando o software. Até logo!")
            # Quebra o loop 'while', finalizando a execução.
            break
        else:
            # Informa o usuário caso a opção digitada não seja válida.
            print("\nOpção inválida. Por favor, escolha uma das opções do menu.")

# --- Ponto de Entrada do Programa ---
# Esta é uma boa prática em Python. O código dentro deste 'if' só executa
# quando o script é rodado diretamente (e não quando é importado por outro script).
if __name__ == "__main__":
    main()
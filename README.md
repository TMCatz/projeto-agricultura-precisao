Projeto Agricultura de Precisão com Python
Protótipo de um software de linha de comando para análise e manejo de solo, desenvolvido como uma ferramenta de apoio à decisão para a agricultura de precisão.

Tabela de Conteúdos
Sobre o Projeto
Funcionalidades
Tecnologias Utilizadas
Como Executar o Projeto
Estrutura do Código
Fluxograma da Aplicação
Autor
Sobre o Projeto

O AgroSolo Tech (nome conceitual do software) é um protótipo de software de terminal desenvolvido em Python, projetado para atuar como uma ferramenta de apoio à decisão para o manejo de solo na agricultura de precisão. Este projeto foi concebido a partir dos conceitos de automação e Agricultura 4.0, com base nos materiais de referência da Embrapa e do Sebrae.

A principal finalidade do software é fornecer diagnósticos rápidos sobre a saúde do solo, analisando dois parâmetros críticos: umidade e níveis de nutrientes (especificamente Nitrogênio). Com base nesses diagnósticos, o sistema gera recomendações imediatas para ações corretivas, como irrigar ou aplicar fertilizantes, auxiliando o agricultor a tomar decisões baseadas em dados para maximizar a eficiência e a sustentabilidade da lavoura.

Funcionalidades
✅ Menu Interativo: Interface de linha de comando clara que permite ao usuário navegar facilmente entre as opções.

✅ Análises Modulares: Possibilidade de executar análises de umidade e nutrientes de forma separada.

✅ Análise Completa e Integrada: Uma opção para rodar todas as análises em sequência e obter um panorama geral.

✅ Validação de Entrada: O sistema é robusto contra entradas inválidas (ex: texto em vez de números), solicitando ao usuário que corrija o dado sem travar a aplicação.

✅ Geração de Relatório: Apresenta um relatório consolidado com os status do solo e recomendações práticas.

✅ Simulação de Ações: Permite ao usuário simular o salvamento do relatório em um sistema local ou o envio para um gestor.

Tecnologias Utilizadas
Python 3
Como Executar o Projeto
Para executar este projeto localmente, siga os passos abaixo.

Pré-requisitos:

Você precisa ter o Python 3 instalado em sua máquina.
Passos:

Clone o repositório:

Bash

git clone https://github.com/TMCatz/projeto-agricultura-precisao.git
Navegue até o diretório do projeto:

Bash

cd projeto-agricultura-precisao
Execute o script Python:

Bash

python AgroSolo Tech.py

Siga as instruções no terminal para interagir com o menu do software.

Estrutura do Código
O software é um script único em Python, mas estruturado de forma modular para garantir a clareza e a manutenibilidade do código.

main(): É a função "cérebro" do programa. Ela controla o menu interativo e orquestra o fluxo de chamadas para as outras funções.
verificar_umidade_solo() e analisar_nutrientes(): Funções especialistas que coletam, validam e analisam um parâmetro específico do solo. Elas usam return para devolver o resultado à função main.
gerar_relatorio_simples(): Função consolidadora que recebe os resultados das análises como parâmetros e os exibe em um formato legível para o usuário.
Fluxograma da Aplicação
O fluxograma abaixo ilustra a arquitetura e o fluxo de navegação do software.

Snippet de código

graph TD
    A([Início]) --> B{Exibir Menu Principal};
    B --> C{Usuário escolhe uma opção};

    C -- Opção 1: Umidade --> D[Executar função verificar_umidade_solo()];
    D --> E[Exibir resultado da umidade na tela];
    E --> B;

    C -- Opção 2: Nutrientes --> F[Executar função analisar_nutrientes()];
    F --> G[Exibir resultado dos nutrientes na tela];
    G --> B;

    C -- Opção 3: Análise Completa --> H[Executar função verificar_umidade_solo()];
    H --> I[Executar função analisar_nutrientes()];
    I --> J[Executar função gerar_relatorio_simples()];
    J --> B;

    C -- Opção 4: Sair --> K[Exibir mensagem "Encerrando..."];
    K --> L([Fim]);
    
    C -- Outra tecla: Inválida --> M[Exibir mensagem "Opção inválida"];
    M --> B;

Autor
Nathan Moratelli


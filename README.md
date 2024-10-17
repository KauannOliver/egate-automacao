# Sistema de Automação e-Gate

Este projeto foi desenvolvido para automatizar o envio de dados de documentos a partir de uma planilha Excel diretamente para o sistema e-Gate. A solução integra automação com Selenium para preencher formulários na web, removendo a necessidade de inserção manual e garantindo maior eficiência no processo.


FUNCIONALIDADES PRINCIPAIS

1. Autenticação Automatizada
O sistema realiza o login no portal e-Gate de forma automática, inserindo as credenciais pré-definidas e autenticando o acesso ao sistema. O uso do Selenium WebDriver garante a execução precisa da automação.

2. Envio de Dados do Excel para o e-Gate
A partir de uma planilha Excel, o sistema lê os dados de documentos e preenche automaticamente os campos correspondentes no formulário web do e-Gate. Isso inclui o número do documento, data de emissão, valor e data de vencimento, que são enviados linha a linha conforme a seleção do usuário.

3. Remoção de Campos Read-Only
Antes de enviar os dados, o sistema remove o atributo "readonly" dos campos de formulário no e-Gate, permitindo a inserção de informações que, de outra forma, não poderiam ser modificadas.

4. Interface Gráfica com Tkinter
A interface gráfica foi construída utilizando a biblioteca Tkinter, permitindo uma interação amigável para o usuário, onde ele pode selecionar a planilha Excel, definir o intervalo de linhas a ser enviado, autenticar o login e visualizar os resultados diretamente na aplicação.

5. Seleção de Arquivo Excel
O sistema oferece uma funcionalidade de seleção de arquivo para que o usuário escolha a planilha Excel de onde os dados serão extraídos. Apenas arquivos .xlsx são permitidos, garantindo compatibilidade com a automação.

6. Exibição de Resultados
Após o envio dos dados, o sistema exibe uma janela com o log detalhado das operações, incluindo o sucesso do envio de cada linha e possíveis erros que ocorreram durante o processo.


TECNOLOGIAS UTILIZADAS

1. Python: Linguagem principal utilizada para o desenvolvimento do back-end e da automação.

2. Tkinter: Biblioteca para criação da interface gráfica, proporcionando uma experiência amigável para o usuário.

3. Selenium: Utilizado para automação de interação com a web, como login, preenchimento de formulários e cliques em botões.

4. Pandas: Biblioteca utilizada para a leitura e manipulação de dados da planilha Excel, garantindo eficiência no processamento.

5. Openpyxl: Utilizada para a leitura de arquivos Excel, extraindo os dados de documentos de forma precisa.

6. WebDriver Chrome: Automação realizada via Selenium, utilizando o navegador Chrome para acessar o sistema e-Gate.


COMO FUNCIONA

O usuário inicia o sistema e seleciona a planilha Excel contendo os dados dos documentos.
Através da interface, o usuário define o intervalo de linhas que deseja enviar para o e-Gate.
O sistema autentica o login automaticamente, acessando o portal e-Gate.
Os dados do Excel são inseridos nos campos do formulário e enviados ao sistema.
Ao final do processo, o sistema exibe um log com os resultados de cada envio.


CONCLUSÃO

Este projeto entrega uma solução robusta para a automação de envio de dados do Excel para o sistema e-Gate, eliminando o trabalho manual e reduzindo o risco de erros na inserção de dados. A combinação de tecnologias como Selenium, Pandas e Tkinter garante uma automação eficiente e fácil de usar, aumentando a produtividade e precisão no envio de informações.

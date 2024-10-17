from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import pandas as pd
import locale
import tkinter as tk

### configura o locale para o formato de número e data do Brasil (pt_BR) ###
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

driver = None  ### variável global para o driver do Selenium ###
msg_text = None  ### variável global para o widget de exibição de mensagens ###

### função para autenticar login na página web ###
def autenticar_login():
    global driver
    driver = webdriver.Chrome()  ### inicializa o WebDriver do Chrome ###

    login = ""  ### define o login ###
    senha = ""  ### define a senha ###

    try:
        ### localiza e preenche o campo de login ###
        campo_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Login"))
        )
        ### localiza e preenche o campo de senha ###
        campo_senha = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "Senha"))
        )
        ### localiza e clica no botão de autenticação ###
        botao_autenticar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn-autenticar"))
        )

        campo_login.send_keys(login)  ### insere o login no campo ###
        campo_senha.send_keys(senha)  ### insere a senha no campo ###
        botao_autenticar.click()  ### clica no botão de autenticação ###

    except Exception as e:
        print(f"Erro ao autenticar login: {str(e)}")  ### exibe mensagem de erro em caso de falha ###

### função para remover o atributo readonly de campos de formulário ###
def remover_readonly():
    driver.execute_script('''
        var inputs = document.querySelectorAll('input[readonly]');  ### seleciona todos os campos readonly ###
        inputs.forEach(function(input) {
            input.removeAttribute('readonly');  ### remove o atributo readonly de cada campo ###
        });
    ''')

### função para enviar os dados do Excel para o formulário web ###
def enviar_dados(linha_inicio, linha_fim, planilha_excel):
    data_de_hoje = datetime.now().date()  ### obtém a data de hoje ###

    df = pd.read_excel(planilha_excel, sheet_name='Testando')  ### carrega os dados da planilha Excel ###

    for index, row in df.iloc[linha_inicio - 1:linha_fim].iterrows():  ### itera sobre as linhas da planilha, conforme intervalo especificado ###
        try:
            ### extrai os dados de cada célula da planilha ###
            txtNumeroDocumento = row['Numero Documento']
            txtDataDocumento = row['Data Documento'].strftime("%d/%m/%Y")
            txtValorDocumento = row['Valor Documento']
            txtDataVencimento = row['Data Vencimento'].strftime("%d/%m/%Y")

            ### localiza e preenche o campo "Número do Documento" no formulário ###
            campo_numerodoc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "txtNumeroDocumento"))
            )
            campo_datadoc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "txtDataDocumento"))
            )
            campo_datarecebimento = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "txtDataRecebimento"))
            )
            campo_datavenc = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "txtDataVencimento"))
            )

            ### formata o valor do documento com separador de milhares ###
            valor_formatado = locale.format_string('%.2f', txtValorDocumento, grouping=True)

            ### insere os dados nos campos do formulário ###
            campo_numerodoc.clear()  ### limpa o campo "Número do Documento" ###
            campo_numerodoc.send_keys(txtNumeroDocumento)  ### insere o número do documento ###

            driver.execute_script(f"document.getElementById('txtValorDocumento').value = '{valor_formatado}';")  ### insere o valor formatado ###

            campo_datadoc.clear()  ### limpa e insere a data do documento ###
            campo_datadoc.send_keys(txtDataDocumento)
            campo_datarecebimento.clear()  ### limpa e insere a data de recebimento ###
            campo_datarecebimento.send_keys(data_de_hoje.strftime("%d/%m/%Y"))
            campo_datavenc.clear()  ### limpa e insere a data de vencimento ###
            campo_datavenc.send_keys(txtDataVencimento)

            ### localiza e clica no botão de enviar ###
            botao_enviar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "lnkAddNota"))
            )
            botao_enviar.click()

            print(f"Dados enviados com sucesso para a linha {index + 1}")  ### exibe mensagem de sucesso ###

        except Exception as e:
            print(f"Erro ao enviar dados para a linha {index + 1}: {str(e)}")  ### exibe mensagem de erro caso falhe ###

### função para abrir a página do e-Gate no navegador ###
def abrir_egate():
    global driver
    driver = webdriver.Chrome()  ### inicializa o WebDriver do Chrome ###
    guia_navegador = "https://egate.fcaservices.com.br/"  ### URL da página a ser acessada ###
    driver.get(guia_navegador)  ### acessa o site ###

### função para exibir os resultados do envio em uma nova janela ###
def mostrar_resultados():
    result_window = tk.Toplevel()  ### cria uma nova janela ###
    result_window.title("Resultados do Envio")  ### define o título da janela ###
    result_window.geometry("600x400")  ### define o tamanho da janela ###
    result_window.configure(background="white")  ### define a cor de fundo ###

    global msg_text
    msg_text = tk.Text(result_window, wrap=tk.WORD, font=("Arial", 12))  ### cria um widget de texto para exibir mensagens ###
    msg_text.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)  ### posiciona o widget de texto na janela ###

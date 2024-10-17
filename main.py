import tkinter as tk
from tkinter import filedialog
import functions as func  ### importa as funções do arquivo functions.py para uso na interface gráfica ###

planilha_excel = None  ### variável global que armazenará o caminho do arquivo Excel selecionado ###
label_arquivo = None  ### variável global para atualizar o nome do arquivo selecionado na interface ###

### função para abrir o diálogo de seleção de arquivo ###
def selecionar_arquivo():
    global planilha_excel, label_arquivo  ### acessa as variáveis globais planilha_excel e label_arquivo ###
    planilha_excel = filedialog.askopenfilename(
        initialdir="/", title="Selecione o arquivo", 
        filetypes=(("Arquivos Excel", "*.xlsx"), ("Todos os arquivos", "*.*"))  ### define os tipos de arquivos permitidos no diálogo ###
    )
    nome_arquivo = planilha_excel.split("/")[-1]  ### obtém apenas o nome do arquivo, sem o caminho completo ###
    label_arquivo.config(text=nome_arquivo)  ### exibe o nome do arquivo na interface ###

### função principal que cria a interface gráfica ###
def main():
    root = tk.Tk()  ### inicializa a janela principal do Tkinter ###
    root.title("Envio de Dados")  ### define o título da janela ###
    root.configure(background="white")  ### define o fundo branco da janela ###

    frame = tk.Frame(root, bg="white")  ### cria um frame dentro da janela para organizar os widgets ###
    frame.pack(padx=10, pady=10)  ### define o espaçamento ao redor do frame ###

    ### cria e posiciona o rótulo para o campo "linha de início" ###
    label_inicio = tk.Label(frame, text="Número da linha de início:", bg="white", font=("Arial", 18))
    label_inicio.grid(row=0, column=0, sticky="w")  ### sticky alinha o texto à esquerda ###

    input_inicio = tk.Entry(frame, font=("Arial", 16), bd=2, relief="groove")  ### campo de entrada para o número da linha de início ###
    input_inicio.grid(row=0, column=1, padx=5, pady=5)  ### posiciona o campo de entrada ###

    ### cria e posiciona o rótulo para o campo "linha de fim" ###
    label_fim = tk.Label(frame, text="Número da linha de fim:", bg="white", font=("Arial", 18))
    label_fim.grid(row=1, column=0, sticky="w")  ### sticky alinha o texto à esquerda ###

    input_fim = tk.Entry(frame, font=("Arial", 16), bd=2, relief="groove")  ### campo de entrada para o número da linha de fim ###
    input_fim.grid(row=1, column=1, padx=5, pady=5)  ### posiciona o campo de entrada ###

    global label_arquivo
    label_arquivo = tk.Label(frame, text="Nenhum arquivo selecionado", bg="white", font=("Arial", 14))  ### rótulo que exibirá o nome do arquivo selecionado ###
    label_arquivo.grid(row=4, column=0, columnspan=2, pady=5)  ### posiciona o rótulo ###

    ### define a função a ser chamada quando o botão "Autenticar Login" for clicado ###
    def handle_autenticar():
        func.autenticar_login()

    ### define a função a ser chamada quando o botão "Enviar Dados" for clicado ###
    def handle_enviar():
        linha_inicio = int(input_inicio.get())  ### pega o valor da linha de início digitado pelo usuário ###
        linha_fim = int(input_fim.get())  ### pega o valor da linha de fim digitado pelo usuário ###
        func.remover_readonly()  ### remove o atributo readonly dos campos no navegador ###
        func.enviar_dados(linha_inicio, linha_fim, planilha_excel)  ### envia os dados das linhas do Excel para o sistema ###

    ### define a função a ser chamada quando o botão "Abrir e-Gate" for clicado ###
    def handle_abrir_egate():
        func.abrir_egate()

    ### define a função a ser chamada quando o botão "Selecionar Planilha" for clicado ###
    def handle_selecionar_arquivo():
        selecionar_arquivo()

    ### define a função para mostrar os resultados do envio ###
    def handle_mostrar_resultados():
        func.mostrar_resultados()

    ### cria o botão de autenticação ###
    button_autenticar = tk.Button(frame, text="Autenticar Login", font=("Arial", 18), bg="#4169E1", fg="white", command=handle_autenticar)
    button_autenticar.grid(row=2, column=1, padx=5, pady=5, sticky="ew")  ### posiciona o botão ###

    ### cria o botão para enviar os dados ###
    button_enviar = tk.Button(frame, text="Enviar Dados", font=("Arial", 18), bg="#4169E1", fg="white", command=lambda: [handle_mostrar_resultados(), handle_enviar()])
    button_enviar.grid(row=3, column=1, padx=5, pady=5, sticky="ew")  ### posiciona o botão ###

    ### cria o botão para abrir o e-Gate ###
    button_abrir_egate = tk.Button(frame, text="Abrir e-Gate", font=("Arial", 18), bg="#4169E1", fg="white", command=handle_abrir_egate)
    button_abrir_egate.grid(row=2, column=0, padx=5, pady=5, sticky="ew")  ### posiciona o botão ###

    ### cria o botão para selecionar o arquivo Excel ###
    button_selecionar_arquivo = tk.Button(frame, text="Selecionar Planilha", font=("Arial", 18), bg="#4169E1", fg="white", command=handle_selecionar_arquivo)
    button_selecionar_arquivo.grid(row=3, column=0, padx=5, pady=5, sticky="ew")  ### posiciona o botão ###

    root.mainloop()  ### inicia o loop principal da interface gráfica ###

if __name__ == "__main__":
    main()  ### chama a função main para iniciar a interface ###

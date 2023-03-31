import PySimpleGUI as sg 
import confirmar_cod as cc
import dados as dados_previsoes

# Janelas

def janela_inicial():
    sg.theme("Dark2")
    layout= [
        [sg.Text("Fazer simulação com:")],
        [sg.Button("Criptomoedas"),sg.Button("Ações")]
    ]
    return sg.Window("Simulação de Monte Carlo", layout=layout, finalize=True)

def janela_cripto():
    sg.theme("Dark2")
    layout=[
        [sg.Text("Insira o código da criptomoeda esolhida:"),sg.Input(key="cod_cripto")],
        [sg.Text("Insira o delay de retirada do valor da moeda (em segundos):"),sg.Input(key="tempo_cripto")],
        [sg.Text("Insira a quantidade de retiradas:"),sg.Input(key="quantidade_de_retiradas_cripto")],
        [sg.Button("Confirmar Cripto")],
        [sg.Button("Voltar")]
    ]
    return sg.Window("Simulação de Monte Carlo para Criptomoedas", layout=layout, finalize=True)

def janela_acao():
    sg.theme("Dark2")
    layout=[
        [sg.Text("Insira o código da ação esolhida:"),sg.Input(key="cod_acao")],
        [sg.Text("Insira o delay de retirada do valor da ação (em segundos):"),sg.Input(key="tempo_acao")],
        [sg.Text("Insira a quantidade de retiradas:"),sg.Input(key="quantidade_de_retiradas_acao")],
        [sg.Button("Confirmar Ação")],
        [sg.Button("Voltar")]
    ]
    return sg.Window("Simulação de Monte Carlo para Ações", layout=layout, finalize=True)

def janela_erro_tempo():
    sg.theme("Dark2")
    layout=[
        [sg.Text("Erro")],
        [sg.Text("Insira um valor em segundos válido")]
    ]
    return sg.Window("Erro", layout=layout, finalize=True)

def janela_erro_cod():
    sg.theme("Dark2")
    layout=[
        [sg.Text("Erro")],
        [sg.Text("Insira um código válido")]
    ]
    return sg.Window("Erro", layout=layout, finalize=True)

def janela_erro_retiradas():
    sg.theme("Dark2")
    layout=[
        [sg.Text("Erro")],
        [sg.Text("Insira um valor inteiro válido")]
    ]
    return sg.Window("Erro", layout=layout, finalize=True)

def janela_previsoes(x,y):
    sg.theme("Dark2")
    layout=[
        [sg.Text("A previsão otimista do ativo é de {}".format(x))],
        [sg.Text("A previsão pessimista do ativo é de {}".format(y))]
    ]
    return sg.Window("Previsão", layout=layout, finalize=True)
# Controle Janelas

janela1, janela2, janela3, janela4, janela5, janela6, janela7 = janela_inicial(), None, None, None, None, None, None
while True:
    window, event, values = sg.read_all_windows()

# Controle ir/voltar janeals:

    if window == janela4 and event == sg.WIN_CLOSED:
        janela4.hide()
    if window == janela5 and event == sg.WIN_CLOSED:
        janela5.hide()
    if window == janela6 and event == sg.WIN_CLOSED:
        janela6.hide()
    if window == janela7 and event == sg.WIN_CLOSED:
        janela7.hide()
    if event == sg.WIN_CLOSED and window != janela4 and window != janela5 and window != janela6 and window != janela7:
        break
    if window == janela1 and event == "Criptomoedas":
        janela2 = janela_cripto()
        janela1.hide()
    if window == janela1 and event == "Ações":
        janela3 = janela_acao()
        janela1.hide()
    if window == janela2 and event == "Voltar":
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == "Voltar":
        janela3.hide()
        janela1.un_hide()

# Conferir se o valor em segundos é válido:

    if window == janela2 and event == "Confirmar Cripto":
        try:
            0+int(values["tempo_cripto"])
        except:
            janela4 = janela_erro_tempo()
        else:
            adress = "https://www.google.com/finance/quote/"+str(values["cod_cripto"])+"-BRL?sa=X&ved=2ahUKEwiXoJPWnZP8AhVNHbkGHW4LBTQQ-fUHegQIBhAe"
            try:
                0+float(cc.confirmar_cod(adress))
            except:
                janela5 = janela_erro_cod()
            else:
                try:
                    0+float(values["quantidade_de_retiradas_cripto"])
                except:
                    janela6 = janela_erro_retiradas()
                else:
                    previsao_otimista, previsao_pessimista = (dados_previsoes.save_data(adress, int(values["tempo_cripto"]), int(values["quantidade_de_retiradas_cripto"])))
                    janela7 = janela_previsoes(previsao_otimista, previsao_pessimista)

            
    if window == janela3 and event == "Confirmar Ação":
        try:
            0+int(values["tempo_acao"])
        except:
            janela4 = janela_erro_tempo()
        else:
            adress = "https://www.google.com/finance/quote/"+str(values["cod_acao"])+":BVMF?sa=X&ved=2ahUKEwiQ4buI8Zf8AhUaHbkGHUWSBGIQ3ecFegQILRAi"
            try:
                0+float(cc.confirmar_cod(adress))
            except:
                janela5 = janela_erro_cod()
            else:
                try:
                    0+int(values["quantidade_de_retiradas_acao"])
                except:
                    janela6 = janela_erro_retiradas()
                else:
                    previsao_otimista, previsao_pessimista = (dados_previsoes.save_data(adress, int(values["tempo_acao"]), int(values["quantidade_de_retiradas_acao"])))
                    janela7 = janela_previsoes(previsao_otimista, previsao_pessimista)
                 
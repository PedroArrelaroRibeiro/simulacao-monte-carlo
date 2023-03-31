import urllib
import urllib.request
import time
import openpyxl
from openpyxl import Workbook
from reta import reta
import pandas as pd
import random as r

def save_data(x,y,z):
    
    # Criar arquivo

    arquivo = Workbook()
    plano = arquivo.active
    plano.title = "Dados"
    arquivo.save("dados.xlsx")

    # Pegar Cotação

    cte0=0
    cte1=2
    
    while True:
        open_adress = urllib.request.urlopen(x)
        codigo_html = str(open_adress.read())
        a=(codigo_html.index("data-last-price="))
        cte0=0
        while True:
            try:
                0+int(codigo_html[a+17+cte0])
            except:
                if codigo_html[a+17+cte0] != ".":
                    break
                cte0=cte0+3
                break
            else:
                cte0=cte0+1 
        cotacao=(codigo_html[a+17:a+17+cte0])
    
    # Atualizar planilha

    # Primeira Linha

        plano["A1"] = "X"
        plano["B1"] = "Y"
        plano["C1"] = "Reta"
        plano["D1"] = "Delta"
        
        plano["E1"] = "S1"
        plano["F1"]  = "S2"
        plano["G1"]  = "S3"
        plano["H1"]  = "S4"
        plano["I1"]  = "S5"
        plano["J1"]  = "S6"
        plano["K1"]  = "S7"
        plano["L1"]  = "S8"
        plano["M1"]  = "S9"
        plano["N1"]  = "S10"

        arquivo.save("dados.xlsx")

    # Coluna A (Númeração da linha)
        plano["A"+str(cte1)] = cte1-1
        arquivo.save("dados.xlsx")

    # Coluna B (Cotação da linha)

        plano["B"+str(cte1)] = cotacao
        arquivo.save("dados.xlsx")

    # Calcular a equação da reta (y=ax+b)

        try:
            a=reta("dados.xlsx")[0]
            b=reta("dados.xlsx")[1]
        except:
            None

    # Coluna C (Reta no ponto)

        tabela = pd.read_excel("dados.xlsx")
        N=len(tabela["X"]) 
        for i in range(N):
            try:   
                plano["C"+str(i+2)] = float(a*(i+1) + b)
                arquivo.save("dados.xlsx")
            except:
                None

    # Coluna D (Delta)

        tabela = pd.read_excel("dados.xlsx")
        tabela["Delta"] = ((tabela["Reta"] - tabela["Y"])**2)**0.5
        tabela.to_excel("dados.xlsx")

    # Desvio Padrão

        media=0
        for i in range(N):
            tabela = pd.read_excel("dados.xlsx")
            media = media + (tabela.loc[i,"Y"])
        media = media  / N

        tabela = pd.read_excel("dados.xlsx")

        dp = 0
        for i in range(N):
            dp = dp + (((float(tabela.loc[i,"Y"]) - media))**2)

        dp = dp/N
        dp = dp**0.5

    # Simulaçoes

        for i in range(10):
            n = r.random()
            tabela["S"+str(i+1)] = (tabela["Reta"])+(-2*dp)+(4*dp*n)
         
        tabela.to_excel("dados.xlsx")
 

    # Previsões
        
        previsao = 0
        n_linha = len(tabela["X"])
        for i in range(10):
            previsao = previsao + (tabela["S"+str(i+1)][n_linha-1])
        previsao = previsao/10

        dp_previsao = 0
        for i in range(10):
            dp_previsao = dp_previsao + (((float(tabela.loc[n_linha-1,"S"+str(i+1)]) - previsao))**2)
        dp_previsao = dp_previsao/10
        dp_previsao = dp_previsao**0.5

        previsao_otimista = previsao + ((2*dp_previsao)/(10**0.5))
        previsao_pessimista = previsao - ((2*dp_previsao)/(10**0.5))
        


    # Relógio
        time.sleep(y)
        cte1=cte1+1
        if cte1==z+2:
            return(previsao_otimista, previsao_pessimista)
import pandas as pd
from IPython.display import display


def reta(x):
    tabela = pd.read_excel(x)
    N=len(tabela["X"])
    if N != 1:
        Sxy=0
        for  i in range(N):
            Sxy=Sxy+(float(tabela.loc[i,"X"])*float(tabela.loc[i,"Y"]))
        Sx=0
        for i in range(N):
            Sx=Sx+float(tabela.loc[i,"X"])
        Sy=0
        for i in range(N):
            Sy=Sy+float(tabela.loc[i,"Y"])
        Sx2=0
        for i in range(N):
            Sx2=Sx2+(float(tabela.loc[i,"X"])**2)

        
        B = (N*Sxy - (Sx)*(Sy)) / (N*Sx2 - (Sx)**2)
        A = (Sy - B*(Sx)) / N

        return B, A
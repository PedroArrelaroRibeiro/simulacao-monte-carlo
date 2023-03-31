import urllib
import urllib.request

def confirmar_cod(x):
    open_adress = urllib.request.urlopen(x)
    codigo_html = str(open_adress.read())
    a=(codigo_html.index("data-last-price="))
    cte0=0
    cte1=0
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
    return cotacao
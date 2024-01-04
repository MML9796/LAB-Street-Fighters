from datetime import date,datetime

def parser_date(cadena,formato="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(cadena,formato)

def parser_booleano(cadena):
    res=None
    if cadena=='1':
        res=True
    elif cadena=='0':
        res=False
    return res 

def parser_cadena(cadena):
    lista=[e.strip() for e in cadena.split(',')]
    return lista 
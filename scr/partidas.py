import csv
from typing import NamedTuple,List,Tuple
from parsers import *
from collections import defaultdict,Counter

Partida = NamedTuple("Partida", [("pj1", str),("pj2", str),("puntuacion", int),("tiempo", float),
    ("fecha_hora", datetime),("golpes_pj1", List[str]),("golpes_pj2", List[str]),("movimiento_final", str),
    ("combo_finish", bool),("ganador", str)])

def lee_partidas(fichero:csv)->List[Partida]:
    partidas=[]
    with open(fichero, encoding='utf-8') as f:
        lector=csv.reader(f)
        next(lector)
        for pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador in lector:
            puntuacion=int(puntuacion)
            tiempo=float(tiempo)
            fecha_hora=parser_date(fecha_hora)
            golpes_pj1=parser_cadena(golpes_pj1)
            golpes_pj2=parser_cadena(golpes_pj2)
            combo_finish=parser_booleano(combo_finish)
            partidas.append(Partida(pj1,pj2,puntuacion,tiempo,fecha_hora,golpes_pj1,golpes_pj2,movimiento_final,combo_finish,ganador))
        return partidas 
    
def victora_mas_rapida(partidas:List[Partida])->Tuple[str,str,float]:
    minimo=None
    for i in partidas:
        if minimo==None or i.tiempo<minimo[2]:
            minimo=(i.pj1,i.pj2,i.tiempo)
    return minimo

def top_ratio_medio_personajes(partidas:List[Partida],n:int)->List[str]:
    dicc=defaultdict(list)
    for i in partidas:
        if i.pj1==i.ganador:
            dicc[i.pj1].append(i.puntuacion/i.tiempo)
        if i.pj2==i.ganador:
            dicc[i.pj2].append(i.puntuacion/i.tiempo)
    ratio=sorted(((nombre,(sum(media)/len(media))) for nombre,media in dicc.items()),key=lambda x:x[1])[:n]
    return [nombre for nombre,_ in ratio]

def enemigos_mas_debiles(partidas:List[Partida],personaje:str):
    dicc=defaultdict(int)
    for i in partidas:
        if personaje==i.ganador and i.pj1!=personaje:
            dicc[i.pj1]+=1
        if personaje==i.ganador and i.pj2!=personaje:
            dicc[i.pj2]+=1
    res=defaultdict(list)
    for nombre,victoria in dicc.items():
        res[victoria].append(nombre)
    return max(res.items(),key=lambda x:x[0])

def movimientos_comunes(partidas:List[Partida],personaje1:str,personaje2:str)->List[str]:
    dicc=defaultdict(list)
    for i in partidas:
        dicc[i.pj1].append(i.golpes_pj1)
        dicc[i.pj2].append(i.golpes_pj2)
    res1=set()
    res2=set()
    for personaje,golpe in dicc.items():
        if personaje1==personaje:
            res1.add(golpe)
        if personaje2==personaje:
            res2.add(golpe)
    return list(res1.intersection(res2))

def dia_mas_combo_finish(partidas:List[Partida])->str:
    dicc=Counter(dia_semana(i.fecha_hora.weekday()) for i in partidas if i.combo_finish==True)
    lista=max(dicc.items(),key=lambda x:x[1])
    return lista[0]
def dia_semana(cadena:int)->str:
    res=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
    return res[cadena]




















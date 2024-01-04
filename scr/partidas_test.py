from partidas import *

def test_lee_partidas(registro:str)->None:
    print(f'Se han leido {len(registro)} partidas')
    print(f'Las tres primeras partidas son: {registro[:3]}')

def test_victoria_mas_rapida(registro:str)->None:
    res=victora_mas_rapida(registro)
    print(f'La victoria más rápida fue entre {res[0]} y {res[1]} y duró {res[2]} segundos')

def test_top_ratio_medio_personajes(registro:str,n:int)->None:
    res=top_ratio_medio_personajes(registro,n)
    print(f'El top {n} de ratios medios es: {res}')

def test_enemigos_mas_debiles(registro:str,personajes:str)->None:
    res=enemigos_mas_debiles(registro,personajes)
    print(f'Los enemigos más débiles del personaje {personajes} son:{res}')

def test_movimientos_comunes(registro:str,personaje1:str,personaje2:str)->None:
    res=movimientos_comunes(registro,personaje1,personaje2)
    print(f'Los movimientos comunes entre {personaje1} y {personaje2} son: {res}')

def test_dia_mas_combo_finish(registro:str)->None:
    res=dia_mas_combo_finish(registro)
    print(f'El día que hubo más combo_finish es: {res}')

if __name__=='__main__':
    datos=lee_partidas('data\games.csv')
    #test_lee_partidas(datos)
    #test_victoria_mas_rapida(datos)
    #test_top_ratio_medio_personajes(datos,3)
    #test_enemigos_mas_debiles(datos,'Ken')
    test_movimientos_comunes(datos,'Ryu','Ken')
    #test_dia_mas_combo_finish(datos)

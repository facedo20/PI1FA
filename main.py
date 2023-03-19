from fastapi import FastAPI
import pandas as pd


app = FastAPI()

@app.get('/')
async def ruta():
    return {'PRIMER API DE FEDERICO ACEDO'}

#cargamos los csv para empezar a trabajar 
listado_gral = pd.read_csv('datsets\ETL.csv')

@app.get('/max')
#funcion 1 : devulve la pelicula con mayor duracion del año indicado segun cada plataforma
def get_max_duration(año:int,tipo_duracion:str, platforma:str):
    nuevalista = listado_gral[(listado_gral['release_year'] == año) &  (listado_gral['duration_type'] == tipo_duracion) & (listado_gral['plataform'] == platforma)]
    nuevalista = nuevalista.loc[nuevalista['duration_int'] == nuevalista['duration_int'].max()]
    result = nuevalista['title']
    return result

@app.get('/cantidad de peliculas')
def get_score_count (plataforma:str,puntaje:float,año:int):
    nuevalist = listado_gral[(listado_gral['plataform'] == plataforma) &  (listado_gral['score'] > puntaje) & (listado_gral['release_year'] == año)]
    result = nuevalist.shape[0]
    return result

@app.get ('/cantidad de peliculas por plataforma')
def get_count_plataform(plataform:str):
    nuevalist =listado_gral[(listado_gral['plataform']==plataform)]
    count=nuevalist.shape[0]
    return count


@app.get ('/actor mas recurrente por año y por plataforma ')
def get_actor(plataform:str, año:int):
    result = listado_gral[(listado_gral['plataform']==plataform) & (listado_gral['release_year']==año)]
    for i in result['cast']:
        if i != 'Sin dato ':
            i=i.replace(', ' , ',')
        else:
            pass
    lista=[]
    for i in result['cast']:
        if i != 'Sin dato':
            s=i.split(',')
            for j in range(len(s)):             
                if s[j] not in lista:
                    lista.append(s[j])
                else:
                    pass
        else:
            pass
    lista=list(set(lista))
    contador = 0
    dict={}
    for i in lista:
        contador = 0
        for j in result['cast']:
            if i in j.split(','):
                contador+=1
        dict[i]=contador
    if len(dict)==0:
        return 'la plataforma no brinda esta informacion'
    else:
        return max(dict,key=dict.get)
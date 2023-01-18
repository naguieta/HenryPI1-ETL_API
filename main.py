from fastapi import FastAPI
import csv
from deta import Deta

#from csvkit.utilities.csvsql import CSVSQL
app = FastAPI()
# Initialize with a Project Key for ztp1zf
deta = Deta("e0d3twub_YfWiW36mbfC1dzk4pvi2bBscK7u93UEJ")
# Set data file path
csvFilePath = r"data2.csv"

# Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
def get_from_title(plataforma,keyword):
    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        cantidad = 0
        for row in csvReader:
            if keyword in row['title'] and row['id'][0] == plataforma[0]:
                cantidad = cantidad + 1
        return cantidad

# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
def get_score_title(plataforma,score,year):
    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        cantidad = 0
        for row in csvReader:
            if row['type'] == 'movie':
                if int(row['score']) > int(score) and row['id'][0] == plataforma[0] and row['release_year'] == year:
                    cantidad = cantidad + 1
        return cantidad

# La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
def get_second_title(plataforma):
    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        puntaje1 = 0
        puntaje2 = 0
        titulo1 = '~'
        titulo2 = '~'
        for row in csvReader:
            if row['id'][0] == plataforma[0]:
                if int(row['score']) >= puntaje1 or int(row['score']) >= puntaje2:
                    if int(row['score']) > puntaje2 or row['title'] < titulo2:
                        titulo2 = row['title']
                        puntaje2 = int(row['score'])
                    if int(row['score']) > puntaje1 or row['title'] < titulo1:
                        titulo2 = titulo1
                        titulo1 = row['title']
                        puntaje2 = puntaje1
                        puntaje1 = int(row['score'])                    
        return titulo2

#Película que más duró según año, plataforma y tipo de duración
def get_longest_title(plataforma,dur_type,year):
    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        duracion = 0
        titulo = ''
        for row in csvReader:
            if row['type'] == 'movie' and row['id'][0] == plataforma[0] and row['release_year'] == year and row['duration_type'] == dur_type and row['duration_int'] != 'nan':
                if int(float(row['duration_int'])) > duracion:
                    duracion = int(float(row['duration_int']))
                    titulo = row['title']
        return titulo

#Película que más duró según año, plataforma y tipo de duración
def get_rating_cvs(rate):
    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)
        cantidad = 0
        for row in csvReader:
            if row['rating'] == rate:
                cantidad = cantidad + 1
        return cantidad
            
@app.get("/")
async def root():    
    return "testing db"

@app.get("/get_word_count/{plataforma}/{keyword}")
def get_keyword_by_platform(plataforma: str, keyword:str ):
    return get_from_title(plataforma,keyword)

@app.get("/get_score_count/{plataforma}/{score}/{year}")
def get_ammount_by_platform(plataforma: str, score:str, year:str ):
    return get_score_title(plataforma,score,year)

@app.get("/get_second_score/{plataforma}")
def get_second_by_platform(plataforma: str):
    return get_second_title(plataforma)

@app.get("/get_longest/{plataforma}/{dur_type}/{year}")
def get_longest_by_platform(plataforma: str, dur_type:str, year:str ):
    return get_longest_title(plataforma,dur_type,year)

@app.get("/get_rating_count/{rate}")
def get_rating(rate: str):
    return get_rating_cvs(rate)
   
@app.get("/ver/")
def demo():
    return "version: 9"

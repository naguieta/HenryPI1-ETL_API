# Proyecto Individual N° 1 de Soy Henry por Nahuel Vargas

## Proyecto sobre Data Engineer - Transformación de datos, elaboración y ejecución de una API.

### Transformación de datos.
Como primer paso de este proyecto se requirió el ajuste de datos sobre los archicos csv ubicados en la carpeta Datasets.
Las modificaciones son las siguientes:
- Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)
- Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”
- De haber fechas, deberán tener el formato AAAA-mm-dd
- Los campos de texto deberán estar en minúsculas, sin excepciones
- Reemplazar las cadenas de texto "Seasons" a "Season" en la columna duration.
- El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

### Desarrollo API
Como segundo paso de este proyecto se requirio la creación y ejecución de una API utilizando el framework FastAPI.
Las condiciones de la API son las siguientes:
- Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
- Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
- La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
- Película que más duró según año, plataforma y tipo de duración
- Cantidad de series y películas por rating

## Instrucciones de uso
Para este proyecto se eligió utilizar la plataforma Deta para hacer el deploy de la aplicacion, el codigo incluido en este Git fue creado y configurado para leer los datos desde el archivo data2.csv y ser compatible con la plataforma Deta.

Una vez que el deploy de este codigo es realizado, la API permite hacer 5 consultas diferentes y devolver información en base a los parametros ingresados en las consultas.

A continuacion se deja un ejemplo por consulta posible, utilizando la URL donde se hizo el deply original. Al final de los ejemplos se pueden observar los posibles valores a utilizar en los parametros.

1. Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.
- *URL/get_word_count/plataforma/keyword*
    - https://0d89d9.deta.dev/get_word_count/netflix/love
        - Respuesta de la API: 196

2. Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
- *URL/get_score_count/plataforma/puntaje/año*
    - https://0d89d9.deta.dev/get_score_count/netflix/85/2010
        - Respuesta de la API: 20

3. La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
- *URL/get_second_score/plataforma*
    - https://0d89d9.deta.dev/get_second_score/amazon
        - Respuesta de la API: "abilene town"

4. Película que más duró según año, plataforma y tipo de duración
- *URL/get_longest/plataforma/tipoDuracion/año*
    - https://0d89d9.deta.dev/get_longest/netflix/min/2016
        - Respuesta de la API: "sairat"

5. Cantidad de series y películas por rating
- *URL/get_rating_count/rating*
    - https://0d89d9.deta.dev/get_rating_count/18+
        - Respuesta de la API: 1243

Parametros disponibles:
   - **plataforma**: amazon - disney - hulu - netflix 
   - **keyword**: cadena de caracteres a buscar.
   - **puntaje**: desde 0 hasta 100
   - **año**: desde 1920 hasta 2021
   - **tipoDuracion**: min si se desea su duracion en minutos, season si se desea su duracion en temporadas
   - **rating**: tipo de clasificacion de la pelicula, a continuacion los posibles valores separados por coma ->
    13+, 16, 16+, 18+, 7+, ages_16_, ages_18_, all, all_ages, g, nc-17, not_rate, nr, pg, pg-13, r, rating, tv-14, tv-g, tv_ma, tv_nr, tv_pg, tv_y, tv_y7, unrated

## Video de demostracion de uso de la API



https://user-images.githubusercontent.com/60989796/213586834-e67101ca-f382-45fb-a5b6-ac7ca65ee484.mp4


## Instrucciones para usar este repositorio
1. Clonar este repositorio.
2. Seguir las siguientes instrucciones para instalar y configurar FastApi y DETA -> 
    https://fastapi.tiangolo.com/deployment/deta/#create-a-free-deta-account
3. Realizar las pruebas en la seccion "Instrucciones de uso" en este archivo. -> https://github.com/naguieta/HenryPI#instrucciones-de-uso
4. *Calificar este proyecto con la máxima puntuación posible.*

